from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
app = Flask(__name__)

app.config['SECRET_KEY'] = 'mdi34bng5903bgfd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#A parte de configurar o login

login_manager= LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id= db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String(100), unique=True)
    password= db.Column(db.String(100))
    name = db.Column(db.String(100))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods= ["GET", "POST"])
def register():
    if request.method== "POST":

        # verificar se o email (user) já e
        if User.query.filter_by(email=request.form.get('email')).first():
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for("login"))

        #é preciso gerar uma senha hash para o novo usuário, passando os parametros necessários
        new_user= User(
            email= request.form.get('email'),
            password= generate_password_hash(password=request.form.get('password'), method="pbkdf2:sha256", salt_length=8),
            name= request.form.get('name'),
        )
        
        db.session.add(new_user)
        db.session.commit()

        #Login e Autenticar o novo usuário depois de adicionar ele no database
        login_user(new_user)

        return redirect(url_for('secrets'))
    return render_template("register.html")


@app.route('/login', methods= ["GET", "POST"])
def login():
    if request.method=="POST":
        email= request.form.get("email")
        password= request.form.get("password")
        #Procurar o usuário no banco de dados pelo email que foi passado
        user= User.query.filter_by(email= email).first()

        #User não existe

        if not user: 
            flash("That email does not exist, please try again.")
            return redirect(url_for("login"))
        
        #Senha errada

        # check_password_hash checa se a senha passada no login é a mesma senha hash do banco de dados
        elif not check_password_hash(user.password, password):
            flash("Password incorrect, please try again.")
            return redirect(url_for("login"))
        
        #Email existe e a senha está correta

        else:
            #Para logar o usuário é preciso usar a função login_user
            login_user(user=user)
            return redirect(url_for("secrets"))
    return render_template("login.html")


@app.route('/secrets')
@login_required
#usar o decorator login_required para acessar essa rota apenas se estiver um login ativo
def secrets():
    #Usar current_user para pegar o usuário atual logado e usar o nome dele como também as outras informações
    print(current_user.name)
    return render_template("secrets.html", name= current_user.name)

@app.route('/logout')
def logout():
    #Para deslogar o usuário, pois se ele continuar logado, será possivel entrar no perfil dele
    logout_user()
    return redirect(url_for("home"))

@app.route('/download')
def download():
    return send_from_directory(directory='static', path="cheat_sheet.pdf")
    


if __name__ == "__main__":
    app.run(debug=True)

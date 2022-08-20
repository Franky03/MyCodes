from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
app = Flask(__name__)

app.config['SECRET_KEY'] = 'mdi34bng5903bgfd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

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
        new_user= User(
            email= request.form.get('name'),
            password= request.form.get('password'),
            name= request.form.get('name'),
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('secrets', name= new_user.name))
    return render_template("register.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/secrets/<name>')
def secrets(name):
    return render_template("secrets.html", name= name)


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    return send_from_directory(directory='static', path="cheat_sheet.pdf")
    


if __name__ == "__main__":
    app.run(debug=True)

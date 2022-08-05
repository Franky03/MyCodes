from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, Length
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key= "senhadoformsqueninguemsabe"
Bootstrap(app)

#Create a Form Class

class LoginForm(FlaskForm):
    email= EmailField(label="Email", validators=[DataRequired()], )
    password= PasswordField(label="Password", validators=[DataRequired(), Length(min=8)])
    submit= SubmitField("Log in")

    #Passar o FlaskForm na Class
    #Inicialmente não precisa de um def init
    #validators serve para alertar se nada for passado no input
    

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods= ["GET", "POST"])
def login():
    form= LoginForm()
    if form.validate_on_submit():
        if form.email.data== "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
        
    return render_template("login.html", form= form)

    # o form vai ser passado como um parametro para o html

# @app.route("/success", )
# def success():
#     return render_template("success.html")

if __name__ == '__main__':
    app.run(debug=True)
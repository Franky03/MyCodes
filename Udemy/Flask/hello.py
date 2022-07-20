from tkinter import Tk
from flask import Flask, render_template
import time


app = Flask(__name__, template_folder="C:/Users/kaiky/OneDrive/Documentos/GitHub/MyCodes/Udemy/WebDevelopment/Portfolio")


@app.route("/")
def hello():
    return "<a href='/username/Franky'>Franky</a><br><a href='/bye/5/6'>Bye</a><br><a href='/index'>Index</a>"

@app.route("/index")
def index():
    return render_template("test.html")

@app.route("/bye/<int:n1>/<int:n2>")
def say_bye(n1, n2):
    return f"{n1}+{n2}= {n1+n2}"

@app.route("/username/<name>")
def name(name):
    return f"<h1>Hello {name}</h1>"\
            "<img src='https://media.giphy.com/media/38U60fvIfokjC/giphy.gif'>"\
            "<h1>GO OUT</h1>"

if __name__== "__main__":   
    app.run(debug=True)
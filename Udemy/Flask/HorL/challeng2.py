from random import randint
from flask import Flask, redirect, render_template, request
import json

app= Flask(__name__, template_folder="C:/Users/kaiky/OneDrive/Documentos/GitHub/MyCodes/Udemy/Flask/HorL")
opt=0


@app.route("/")
def init():
    print(opt)
    return render_template("index.html", opt= opt)


@app.route("/", methods = ['POST'])
def test():
    global opt
    output= request.get_json()
    print(output, type(output))

    num= json.loads(output)
    print(num, type(num))

    opt=num['number']
    print(opt)

    return redirect(f'/{opt}')


@app.route(f"/{opt}")
def menor():
    return render_template(f"maior.html")


if __name__== "__main__":
    app.run(debug=True)
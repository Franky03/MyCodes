from random import randint
from flask import Flask, redirect, render_template, request
import json

app= Flask(__name__, template_folder="C:/Users/kaiky/OneDrive/Documentos/GitHub/MyCodes/Udemy/Flask/HorL")
opt=0


@app.route("/")
def init():
    return render_template("index.html")


@app.route("/", methods = ['POST'])
def test():
    global opt
    output= request.get_json()
    print(output, type(output))

    num= json.loads(output)
    print(num, type(num))

    opt=num['number']

    return opt

random_number= randint(0, 9)
print(random_number)

@app.route("/<int:num>")
def menor(num):
    if num>random_number:
        return render_template("maior.html")
    elif num<random_number:
        return render_template("menor.html")
    else:
        return render_template("igual.html")


if __name__== "__main__":
    app.run(debug=True)
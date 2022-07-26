from random import randint
from flask import Flask, redirect, render_template, request
import json

app= Flask(__name__)
opt=0


@app.route("/")
def init():
    global random_number
    random_number= randint(0, 9)
    print(random_number)
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
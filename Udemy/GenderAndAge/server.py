from flask import Flask, render_template
import requests


app= Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/guess/<string:name>")
def guess(name):
    age= requests.get(f"https://api.agify.io?name={name}").json()['age']
    gender= requests.get(f"https://api.genderize.io?name={name}").json()["gender"]
    return render_template("guessed.html", name= name, gender= gender, age= age)

if __name__=="__main__":
    app.run(debug=True)
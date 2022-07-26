from datetime import datetime
import random
from flask import Flask, render_template
import requests

app= Flask(__name__)

@app.route("/")
def hello():
    random_number= random.randint(1, 10)
    year= datetime.now().year
    
    return render_template("index.html", num= random_number, year= year)

@app.route("/blog/<num>")
def get_blog(num):
    response=requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("blog.html", posts= response)

if __name__=="__main__":
    app.run(debug=True)
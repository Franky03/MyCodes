from flask import Flask, render_template, request

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods= ["POST"]) #Metodo post nos parametros, pode ser o GET e o POST AO MESMO TEMPO
def receive_data():
    name= request.form["username"].title() #Para pegar o input tem de usar o método request do próprio flask
    password= request.form["password"]
    return f"<h1>Name: {name}, Password: {password}</h1>"

if __name__=="__main__":
    app.run(debug=True)



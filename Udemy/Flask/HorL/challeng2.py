from flask import Flask, render_template

app= Flask(__name__, template_folder="C:/Users/kaiky/OneDrive/Documentos/GitHub/MyCodes/Udemy/Flask/HorL")

@app.route("/")
def init():
    return render_template("index.html")

if __name__== "__main__":
    app.run(debug=True)
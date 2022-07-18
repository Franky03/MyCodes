from flask import Flask, render_template
import time

#Python Decorator Function

# def decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         #Do something before
#         function()
#         function()
#         #Do something after
#     return wrapper_function

# @decorator
# def say_hello():
#     print("Hello")

# say_hello()

# def say_bye():
#     print("Bye")

# say_bye()

app = Flask(__name__, template_folder="C:/Users/kaiky/OneDrive/Documentos/GitHub/MyCodes/Udemy/WebDevelopment/Portfolio")

@app.route("/")
def hello():
    return "<h1>Hello</h1>"

@app.route("/index")
def index():
    return render_template("test.html")

@app.route("/bye")
def say_bye():
    return "<p>Bye</p>"

if __name__== "__main__":   
    app.run()
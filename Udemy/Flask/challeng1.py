from flask import Flask

app= Flask(__name__)

def make_bold(function):
    def bolded():
        return f"<b>{function()}</b>"
    return bolded

def make_emphasis(function):
    def emphasis():
        return f"<em>{function()}</em>"
    return emphasis

def make_underlined(function):
    def underlined():
        return f"<u>{function()}</u>"
    return underlined

@app.route('/')
@make_bold
@make_emphasis
@make_underlined
def hello():
    return "<p>Hello World</p>"

if __name__== "__main__":
    app.run(debug= True)

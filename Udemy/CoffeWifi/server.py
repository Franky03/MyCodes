from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, URL
import csv

app= Flask(__name__)
app.config["SECRET_KEY"] = "88rghteopln447n4s21"
Bootstrap(app)

class CreateForm(FlaskForm):
    name= StringField("Cafe Name", validators= [DataRequired()])
    location= StringField("Location on Google Maps", validators= [DataRequired(), URL()])
    open_= StringField("Opening Time e.g 7AM", validators= [DataRequired()])
    close_= StringField("Closing Time e.g 6:30PM", validators= [DataRequired()])
    coffe= SelectField("Coffe Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators= [DataRequired()])
    wifi= SelectField("Wifi Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators= [DataRequired()])
    power= SelectField("Power Socket Availability", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators= [DataRequired()])
    submit= SubmitField("Submit")


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/add', methods= ['GET', 'POST'])
def add():
    form= CreateForm()
    if form.validate_on_submit():
        with open("./Udemy/CoffeWifi/cafe-data.csv", mode='a', encoding="utf8") as cafe_file:
            cafe_file.write(f"\n{form.name.data},"
                            f"{form.location.data},"
                            f"{form.open_.data},"
                            f"{form.close_.data},"
                            f"{form.coffe.data},"
                            f"{form.wifi.data},"
                            f"{form.power.data}")

        return redirect(url_for('add'))
    return render_template("add.html", form= form)

@app.route('/cafes') 
def cafes():
    with open("./Udemy/CoffeWifi/cafe-data.csv", newline='', encoding="utf8") as cafe:
        csv_data= csv.reader(cafe, delimiter=',')
        all_cafes=[]
        for r in csv_data:
            all_cafes.append(r)
    return render_template('cafes.html', rows= all_cafes)



if __name__== "__main__":
    app.run(debug=True)
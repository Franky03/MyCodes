from random import choice
from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def goto_dict(self):
        dict={}
        for column in self.__table__.columns:
            #Criar uma nova entrada do dicionário
            #Onde a key é o nome da coluna e os valores são os valores dela
            dict[column.name]= getattr(self, column.name)
        return dict



db.create_all()


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


@app.route("/random")
def random():
    all_coffes= db.session.query(Cafe).all()
    random_cafe= choice(all_coffes)
    #Simply convert the random_cafe data record to a dictionary of key-value pairs.
    return jsonify(cafe= random_cafe.goto_dict())
    

@app.route("/all")
def all_cafes():
    all_coffes= db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.goto_dict() for cafe in all_coffes])

@app.route("/search")
def search():
    query_location= request.args.get("loc")
    cafe= Cafe.query.filter_by(location= query_location).first()
    if cafe:
        return jsonify(cafe= cafe.goto_dict())
    return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})

@app.route("/add", methods= ["POST"])
def add():
    new_cafe= Cafe(
        name= request.form.get("name"),
        map_url= request.form.get("map_url"),
        img_url= request.form.get("img_url"),
        location= request.form.get("location"),
        seats= request.form.get("seats"),
        has_toilet= bool(request.form.get("has_toilet")),
        has_wifi= bool(request.form.get("has_wifi")),
        has_sockets= bool(request.form.get("has_sockets")),
        can_take_calls= bool(request.form.get("can_take_calls")),
        coffee_price= request.form.get("coffee_price")
        )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response= {"success": "Successfully added the new cafe."})
## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)

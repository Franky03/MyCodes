from flask import Flask, render_template, redirect, url_for, request
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
#CRIAR A DATABASE
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///new-books-collection.db"
#OPCIONAL (VAI SILENCIAR AS ATUALIZAÇÃO NO CONSOLE)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db= SQLAlchemy(app)

#CRIAR A TABLE
class Book(db.Model):
    id= db.Column(db.Integer, primary_key= True)
    title= db.Column(db.String(250), unique= True, nullable= False)
    author= db.Column(db.String(250), nullable= False)
    rating= db.Column(db.Float, nullable= False)
    
    #OPCIONAL: VAI PERMITIR QUE CADA LIVRO SEJA IDENTIFICADO PELO SEU TITULO QUANDO PRINTADO
    def __repr__(self):
        return f'<Book {self.title}>'

db.create_all()

#CRIAR UM NOVO LIVRO
new_book= Book(id=1, title= 'Harry Potter', author= 'J.K. Rowling', rating= 9.8)
db.session.add(new_book)
db.session.commit()
        
# db= sqlite3.connect("./Udemy/LibSQLite/books-collection.db")
# cursor= db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

@app.route("/")
def home():
    return render_template("index.html", books= db)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method=="POST":
        dados= request.form

        new_book= {
            "title": dados['title'],
            "author": dados['autor'], 
            "rating": dados["rating"]
        }

        
        return redirect(url_for('home'))

    return render_template("add.html")

if __name__== "__main__":
    app.run()
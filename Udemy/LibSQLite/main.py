from flask import Flask, render_template, redirect, url_for, request, session
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

# new_book= Book(id=1, title= 'Harry Potter', author= 'J.K. Rowling', rating= 9.8)
# db.session.add(new_book)
# db.session.commit()

# db= sqlite3.connect("./Udemy/LibSQLite/books-collection.db")
# cursor= db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


@app.route("/")
def home():
    all_books= Book.query.all()
    return render_template("index.html", books= all_books)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method=="POST":
        dados= request.form
        #Criando um novo livro no database
        new_book= Book(title= dados["title"], author= dados["autor"], rating= dados["rating"])
        db.session.add(new_book)
        db.session.commit()
        
        return redirect(url_for('home'))

    return render_template("add.html")

@app.route("/edit", methods= ['GET', 'POST'])
def edit():
    if request.method== 'POST':
        #É preciso pegar o id e o livro especifico novamente pq o está na sessão de POST
        #O book_selected não vai funcionar aqui pq está depois do if

        book_id= request.form['id']
        book_to_update= Book.query.get(book_id)
        book_to_update.rating= request.form['rating']
        db.session.commit()
        return redirect(url_for('home'))

    book_id= request.args.get('id') #Pegar o id enviado pelo url_for do index (Edit Rating)
    book_selected= Book.query.get(book_id) #Pegar o livro selecionado
    return render_template("edit_rating.html", book= book_selected)

@app.route('/delete')
def delete():
    book_id= request.args.get('id')
    book_to_delete= Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__== "__main__":
    app.run(debug=True)
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired
import requests
from sqlalchemy import desc

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///movies-colection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db= SQLAlchemy(app)

#Classes para os sites

class Movie(db.Model):
    id= db.Column(db.Integer, primary_key= True)
    title= db.Column(db.String(250), unique= True, nullable=False)
    year= db.Column(db.Integer, nullable= False)
    description= db.Column(db.String(250), nullable=False)
    rating= db.Column(db.Float)
    ranking= db.Column(db.Integer)
    review= db.Column(db.String(250), unique= False)
    img_url= db.Column(db.String(250), nullable= False)

    def __repr__(self):
        return f'<Book {self.title}>'

db.create_all()

class UpdateMovie(FlaskForm):
    new_rating= StringField(label='Your Rating Out of 10 e.g. 7.5')
    new_review= StringField(label='Your Review')
    submit= SubmitField('Done')

class AddMovie(FlaskForm):
    title= StringField(label="Movie Title", validators=[DataRequired()])
    submit= SubmitField('Done')

#Páginas

@app.route("/")
def home():
    all_movies= Movie.query.order_by(desc(Movie.rating)).all()
    for index in range(len(all_movies)):
        all_movies[index].ranking= index + 1
    
    db.session.commit()

    return render_template("index.html", movies= all_movies)

@app.route('/edit', methods= ['GET', 'POST'])
def edit():
    form= UpdateMovie()
    movie_id= request.args.get('id')
    movie_selected= Movie.query.get(movie_id)
    if form.validate_on_submit():
        if form.new_rating.data != '':
            movie_selected.rating= float(form.new_rating.data)
        if form.new_review.data != '':
            movie_selected.review= form.new_review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", form= form, movie= movie_selected)

@app.route('/delete')
def delete():
    movie_id= request.args.get('id')
    movie_selected= Movie.query.get(movie_id)
    db.session.delete(movie_selected)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/add', methods=['GET', 'POST'])
def add():
    form= AddMovie()
    if form.validate_on_submit():
        movie_title= form.title.data
        response= requests.get('https://api.themoviedb.org/3/search/movie', params={'api_key': 'f49c37daac434354e7db8f0537ff98fa', 'query': movie_title, 'include_adult': True})
        data= response.json()['results']
        return render_template('select.html', data=data)
    return render_template('add.html', form=form)

@app.route('/find')
def find_movie():
    movie_id= request.args.get('id')
    if movie_id:
        response= requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}', params={'api_key': 'f49c37daac434354e7db8f0537ff98fa', "language": "pt-br"})
        data= response.json()
        
        new_movie= Movie(
            title= data['title'],
            year= data['release_date'].split('-')[0],
            description= data['overview'],
            img_url= f"https://image.tmdb.org/t/p/w500{data['poster_path']}"                           
        )

        db.session.add(new_movie)
        db.session.commit()

    return redirect(url_for('edit', id= new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)

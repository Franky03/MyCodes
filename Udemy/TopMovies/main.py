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

with app.app_context():
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
    #Ordenei a lista da database por ordem decrescente de rating, que vai ser ordem crescente do ranking
    all_movies= Movie.query.order_by(desc(Movie.rating)).all() 
    #Depois coloquei os rankings de acordo com a lista ordenada
    for index in range(len(all_movies)):
        all_movies[index].ranking= index + 1 
    
    db.session.commit()

    return render_template("index.html", movies= all_movies)

@app.route('/edit', methods= ['GET', 'POST'])
def edit():
    form= UpdateMovie()
    #Peguei o id do filme que vai ser atualizado pelo url_for do index
    movie_id= request.args.get('id')
    #Movie selecionado foi pego pelo metodo query usando o id
    movie_selected= Movie.query.get(movie_id) 
    #Depois é só atualizar o rating e o review se forem passados, respectivamente
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
    #Aqui eu criei uma rota para deletar, não necessáriamente precisa de um arquivo html para ser renderizado
    movie_id= request.args.get('id')
    movie_selected= Movie.query.get(movie_id)
    db.session.delete(movie_selected)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/add', methods=['GET', 'POST'])
def add():
    form= AddMovie()
    #Nessa página será adicionado um novo filme, aparecerá uma lista de possiveis filmes que o cliente irá pesquisar
    if form.validate_on_submit():
        movie_title= form.title.data
        #usando a api do the movie db
        response= requests.get('https://api.themoviedb.org/3/search/movie', params={'api_key': 'MY_API_KEY', 'query': movie_title, 'include_adult': True})
        data= response.json()['results']
        #É nessa parte que será renderizado uma nova página, a de seleção dos filmes encontrados da api
        return render_template('select.html', data=data)
    return render_template('add.html', form=form)

@app.route('/find')
def find_movie():
    #Aqui é usado um outro json mas com a mesma api, só que dessa vez é com o filme que o cliente escolheu, a api irá pegar os dados do filme
    movie_id= request.args.get('id')
    if movie_id:
        #A linguagem escolhida foi portugues mas pode ser selecionada outra linguagem como inglês
        response= requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}', params={'api_key': 'MY_API_KEY', "language": "pt-br"})
        data= response.json()
        #Adicionaremos o novo filme para a nossa database
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

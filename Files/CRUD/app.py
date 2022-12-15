from flask import Flask, Response, request, render_template
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json

app= Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] =  "sqlite:///dtbs.db"

db= SQLAlchemy(app)

class User(db.Model):
    
    id= db.Column(db.Integer, primary_key= True, unique=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100))
    
    def to_json(self):
        return {"id": self.id, "nome": self.nome, "email": self.email}

def gera_response(status, name, conteudo, msg=False):
    body= {}
    body[name]= conteudo
    if(msg):
        body[msg]= msg
    
    return Response(json.dumps(body), status= status, mimetype= "application/json")

#Selecionar tudo
@app.route("/users", methods= ["GET"])
def select_all():   
    users_objects= User.query.all()
    print(users_objects)
    users_json= [user.to_json() for user in users_objects]
    print(users_json)
    return gera_response(200, "users", users_json, "ok")


#Selecionar um
@app.route("/user/<id>", methods=['GET'])
def select_user(id):
    user_object= User.query.filter_by(id=id).first()
    user_json= user_object.to_json()

    return gera_response(200, 'user', user_json)

#Cadastrar
@app.route("/user", methods=['POST'])
def create():
    body= request.get_json()

    #validation or try catch

    try:
        new_user= User(nome= body["nome"], email= body["email"])
        db.session.add(new_user)
        db.session.commit()

        return gera_response(200, "user", new_user.to_json(), "Criado com sucesso")
    except Exception as e:
        print(e)
        return gera_response(400, 'user', {}, "Erro ao cadastrar")

#Atualizar
@app.route("/user/<id>", methods=['PUT'])
def update(id):
    #Pega usuario e request
    user_object= User.query.filter_by(id=id).first()
    body= request.get_json()
    try:
        if('nome' in body):
            user_object.nome= body["nome"]
        if('email' in body):
            user_object.email= body["email"]
        db.session.add(user_object)
        db.session.commit()
        return gera_response(200, "user", user_object.to_json(), "Atualizado com sucesso")

    except Exception as e:
        print(e)
        return gera_response(400, 'user', {}, "Erro ao cadastrar")
#Deletar
@app.route('/user/<id>', methods=['DELETE'])
def delete(id):
    user_object= User.query.filter_by(id=id).first()
    try:
        db.session.delete(user_object)
        db.session.commit()
        return gera_response(200, "user", user_object.to_json(), "Deletado com sucesso")
    except Exception as e:
        print(e)
        return gera_response(400, 'user', {}, "Erro ao deletar")

if __name__=='__main__':
    app.run(debug=True)
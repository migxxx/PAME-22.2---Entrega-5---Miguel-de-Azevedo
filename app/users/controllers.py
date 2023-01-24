from flask import request
from flask.views import MethodView

from .schemas import UserSchema
from .models import Users

# /users
class UserController(MethodView): # classe de controle de usuarios

    def get(self):                  # get all users
        schema = UserSchema()
        users = Users.query.all()

        return schema.dump(users, many = True), 200

    def post(self):                 # create a user with the last ID
        schema = UserSchema()
        data = request.json

        try:
            user = schema.load(data)
        except:
            return {}, 400

        user.save()

        return schema.dump(user), 201

        # OBS: É interessante implementar uma senha padrão para o sistema, simulando um cofre,\
        # assim ao realizar o post, o usuário solicitante é perguntado qual a senha padrão, fazendo uma segurança básica do software
        # e impossibilitando de pessoas que não são funcionários acessarem funções essenciais.

        # Tal senha padrão pode ser implementada pelo Front-End, por se tratar de uma interação com o usuário.

        # EXEMPLO REAL: Quem tem TV da NET sabe, que ao acessar um canal que está tendo algum filme de classificação 16+ \
        # é necessário introduzir uma senha (que normalmente é 0000) para continuar.


# /users/<id>
class UserDetails(MethodView): # classe de detalhes de um usuario

    def get(self,id):
        schema = UserSchema()

        user = Users.query.get(id)
        if not user:
            return {"error": "user not found"}, 404
        
        return schema.dump(user), 200

    def put(self, id):
        schema = UserSchema()

        user = Users.query.get(id)
        if not user:
            return {"error": "user not found"}, 404
        
        data = request.json
        try:
            user = schema.load(data, instance=user)
        except:
            return {}, 400

        user.save()
        return schema.dump(user), 201


    def patch(self, id):
        schema = UserSchema()

        user = Users.query.get(id)
        if not user:
            return {"error": "user not found"}, 404
        
        data = request.json

        try:
            user = schema.load(data, instance=user, partial = True) # partial = True, significa que o dado pode ser mudado parcialmente, mantendo suas outras caracteristicas
        except:
            return {}, 400

        user.save()
        return schema.dump(user), 201


    def delete(self, id):

        user = Users.query.get(id)
        if not user:
            return {"error": "user not found"}, 404
        
        user.delete(user)
        return{}, 204
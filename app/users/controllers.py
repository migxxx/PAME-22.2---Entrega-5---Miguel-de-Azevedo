from flask import request
from flask.views import MethodView

from .schemas import UserSchema, LoginSchema
from .models import Users

from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

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
            user = schema.load(data) # carrega os dados do usuario
        except:
            return {}, 400

        user.save() # salva o usuario no banco de dados

        return schema.dump(user), 201


# /users/<id>
class UserDetails(MethodView): # classe de detalhes de um usuario

    decorators = [jwt_required()] # decorator para proteger a rota

    def get(self,id):
        schema = UserSchema()

        user = Users.query.get(id)

        if id != get_jwt_identity():
            return {"error": "invalid credentials"}, 401
        if not user:
            return {"error": "user not found"}, 404
        
        return schema.dump(user), 200

    def put(self, id):
        schema = UserSchema()

        user = Users.query.get(id) # pega o usuario pelo id
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
            user = schema.load(data, instance=user, partial = True) # carrega os dados do usuario, porem com o (partial = True) que significa que os dados podem ser mudados parcialmente, mantendo suas outras caracteristicas
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

# binario (senha.encode), bcrypt.gensalt(adiciona textos aleatorios), bcrypt.hashpw (transforma a senha em hash)

class UserLogin(MethodView):
    def post(self):
        schema = LoginSchema()
        data = schema.load(request.json) 

        user = Users.query.filter_by(username = data["username"]).first() # filtra o usuario pelo username

        if not user:
            return {"error": "user not found"}, 404

        if not user.check_password(data["password"]): # verifica se a senha esta correta
            return {"error": "invalid password"}, 401

        token = create_access_token(identity = user.id) # cria um token de acesso com o id do usuario

        return {"user": UserSchema().dump(user), "token": token}, 200
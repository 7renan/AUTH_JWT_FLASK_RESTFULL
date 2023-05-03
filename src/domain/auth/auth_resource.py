import jwt
from flask_restful import Api, Resource
from flask import request, jsonify, make_response
from src.data import user


class Accounts(Resource):

    def get(self):
        return {
            "Message": "Welcome to AUTHJWT API"
        }, 200

    def post(self):
        data = {
            'name': request.form.get('name'),
            'password': request.form.get('password')
        }

        if data != user:
            return {
                'Message': 'User not found'
            }, 401

        token_user = jwt.encode(user, "secret", algorithm='HS256')

        return {
            'token': token_user,
            'user': user
        }, 200


auth_api = Api()
auth_api.add_resource(Accounts, '/', '/login')

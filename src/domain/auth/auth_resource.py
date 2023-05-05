import jwt
from flask_restful import Api, Resource
from flask import request, jsonify, make_response
from src.data import user
from datetime import datetime, timedelta

# parser
from src.config.http.reqparse_config import ParseConfig

parse_config = ParseConfig.get_parse()
parse_config_authorization = ParseConfig.get_parse_authorization()


class Auth(Resource):

    def post(self):

        parse_config.add_argument('name', required=True)
        parse_config.add_argument('password', required=True)

        args = parse_config.parse_args()

        data = {
            'name': args['name'],
            'password': args['password']
        }

        if user['name'] != data['name'] and user['password'] != data['password']:
            return {
                "Message": "User Not Found"
            }, 401

        token_user = jwt.encode(user, "secret", algorithm='HS256')

        return {
            'token': token_user,
            'user': {
                'name': user['name']
            }
        }, 200


class VerifyUser(Resource):

    def get(self):
        args = parse_config_authorization.parse_args()
        user_token = args['Authorization'].split(' ')[1]
        decoded_token = jwt.decode(user_token, "secret", algorithms=['HS256'])
        return decoded_token

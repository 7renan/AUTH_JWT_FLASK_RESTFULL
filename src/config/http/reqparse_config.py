from flask_restful import reqparse


class ParseConfig:

    @staticmethod
    def get_parse():
        parse = reqparse.RequestParser()
        return parse

    @staticmethod
    def get_parse_authorization():
        parse = reqparse.RequestParser()
        parse.add_argument(
            'Authorization', required=True, location='headers')
        return parse

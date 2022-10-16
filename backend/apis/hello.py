from flask_restx import Resource
from flask import request


class HelloWorld(Resource):
    def get(self):
        return {'data': [{'name': 'Vikrame', 'age': 23}, {'name': 'John', 'age': 29}]}

    def post(self):
        json = request.json
        print(type(json), json)
        return {'message': 'successful'}

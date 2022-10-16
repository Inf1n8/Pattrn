from flask_restx import Resource
from flask import request
from .schema.schema_def import LoginSchema
from marshmallow.exceptions import ValidationError


class Login(Resource):
    def post(self):
        data = request.json
        try:
            data = LoginSchema().load(data)
        except ValidationError as err:
            return {'message': err.messages}, 400
        if data['email'] == "abc@usc.edu" and data['password'] == "admin":
            return {'message': 'Authentication successful'}, 200
        return {'message': 'Invalid credentials'}, 401

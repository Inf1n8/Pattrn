from flask_restx import Resource
from flask import request
from .schema.schema_def import LoginSchema
from marshmallow.exceptions import ValidationError
from apis.database import check_login_data


class Login(Resource):
    def post(self):
        data = request.json
        try:
            data = LoginSchema().load(data)
        except ValidationError as err:
            return {'message': err.messages}, 400
        print("Nice")
        return check_login_data(email=data['email'], password=data['password'])

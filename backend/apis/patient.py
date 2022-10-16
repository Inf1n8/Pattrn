import uuid
from flask_restx import Resource
from flask import request
from marshmallow.exceptions import ValidationError
from .schema.schema_def import PatientSchema


class Patients(Resource):
    def post(self):
        data = request.json
        data['id'] = uuid.uuid4().hex
        try:
            data = PatientSchema().load(data)
        except ValidationError as err:
            return {'message': err.messages}, 400
        return {'message': 'OK'}  # Remove after integrating with DB
        # res = insert_patient_data(data)
        # return res


class PatientDetail(Resource):
    def get(self, id):
        if not id:
            return {'message': 'Patient ID was not provided'}, 400
        # res = fetch_patient_detail(id)
        # return res

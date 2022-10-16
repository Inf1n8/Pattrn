import uuid
from flask_restx import Resource
from flask import request
from marshmallow.exceptions import ValidationError
from .schema.schema_def import PatientSchema
from apis.database import post_login_data, get_fhir_id
from apis.fhir_database import get_patient_data, insert_patient_data
from http import HTTPStatus
import json


class Patients(Resource):
    def post(self):
        data = request.json
        try:
            data = PatientSchema().load(data)
            fhir_id = insert_patient_data(data)
            id = post_login_data(data['email'], data['password'], fhir_id)
            return {"message": "Successfully inserted", "id": str(id)}, HTTPStatus.ACCEPTED
        except ValidationError as err:
            return {'message': err.messages}, 400
        return {'message': 'OK'}  # Remove after integrating with DB
        # res = insert_patient_data(data)
        # return res


class PatientDetail(Resource):
    def get(self, id):
        fhir_id = get_fhir_id(id)
        patient_response = get_patient_data(fhir_id)
        return json.dumps(patient_response), HTTPStatus.OK
        if not id:
            return {'message': 'Patient ID was not provided'}, 400
        # res = fetch_patient_detail(id)
        # return res

from flask_restx import Resource
from flask import request
from marshmallow.exceptions import ValidationError
from .schema.schema_def import PatientSchema
from apis.database import post_login_data, get_fhir_id
from apis.fhir_database import get_allergy_info,put_allergy_info
from http import HTTPStatus
import json

baseDict = {'resource': {
    "resourceType": "Goal",
    "id": "set goals",
    "subject": {
        "reference": "Patient/"
    },
    "target": [
        {
            "measure": {
                "coding": [
                    {
                        "system": "http://loinc.org",
                        "code": "3141-9"
                    }
                ]
            },
            "detailRange": {
                "low": {
                    "value": 0,
                    "unit": ""
                },
                "high": {
                    "value": 0,
                    "unit": ""
                }
            }
        }
    ],
},

    'request': {'method': 'POST', 'url': 'Goal'}}


class AllergyData(Resource):
    def get(self, id):
        fhir_id = get_fhir_id(id)
        patient_response = get_allergy_info(fhir_id)
        data={}
        dataDict=patient_response["entry"][-1]["resource"]
        data["allergent"]=dataDict["code"]["coding"][0]["display"]
        data["category"]=dataDict["category"]
        data["reaction"]=dataDict["reaction"][0]["description"]
        return data, HTTPStatus.OK

    def post(self, id):
        data = request.json
        fhir_id = get_fhir_id(id)
        try:
            cnt = put_allergy_info(fhir_id, data)
            return {"message": "Successfully inserted", "numGoals": str(cnt)}, HTTPStatus.ACCEPTED
        except ValidationError as err:
            return {'message': err.messages}, 400
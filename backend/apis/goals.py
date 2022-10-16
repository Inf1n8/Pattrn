import uuid
from flask_restx import Resource
from flask import request
from marshmallow.exceptions import ValidationError
from .schema.schema_def import PatientSchema
from apis.database import post_login_data, get_fhir_id
from apis.fhir_database import get_goal_data, insert_goal_data
from http import HTTPStatus
import json
baseDict={'resource':{
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

class Goals(Resource):
    def post(self,id):
        data = request.json
        fhir_id = get_fhir_id(id)
        print("FHIR_ID",fhir_id)
        try:
            cnt = insert_goal_data(fhir_id,data)
            return {"message": "Successfully inserted", "numGoals": str(cnt)}, HTTPStatus.ACCEPTED
        except ValidationError as err:
            return {'message': err.messages}, 400


class GoalDetail(Resource):
    def get(self, id):
        fhir_id = get_fhir_id(id)
        patient_response = get_goal_data(fhir_id)
        return json.dumps(patient_response), HTTPStatus.OK
        if not id:
            return {'message': 'Patient ID was not provided'}, 400
        # res = fetch_patient_detail(id)
        # return res

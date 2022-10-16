import uuid
from flask_restx import Resource
from flask import request
from marshmallow.exceptions import ValidationError
from apis.database import  get_fhir_id
from apis.fhir_database import insert_observations
from http import HTTPStatus

baseDict={'resource': {'resourceType': 'Observation',
 'status': 'final',
 'code': {'coding': [{'system': 'https://terminology.hl7.org/CodeSystem/observation-category',
    'code': 'activity',
    'display': 'activity'}]},
 'subject': {'reference': 'Patient/'},
 'effectiveDateTime': '',
 'issued': '',
 'valueQuantity': {'value': 0,
  'unit': '',
  'system': 'https://unitsofmeasure.org',
  'code': ''}},
   'request': {'method': 'POST', 'url': 'Observation'}}

class Observations(Resource):
    def post(self,id):
        data = request.json 
        #List of Dictionaaries where each Dict is of format
        # it={
        #     "effectiveDateTime":"2022-10-13T00:00:00+00:00",
        #     "issued":"2022-10-13T00:00:00+00:00",
        #     "value":3228,
        #     "unit":"steps"
        #     }
        fhir_id = get_fhir_id(id)
        try:
            cnt = insert_observations(fhir_id,data,baseDict)
            return {"message": "Successfully inserted", "numObservations": str(cnt)}, HTTPStatus.ACCEPTED
        except ValidationError as err:
            return {'message': err.messages}, 400


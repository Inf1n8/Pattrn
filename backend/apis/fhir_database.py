from fhir.resources.patient import Patient
import requests
from fhir.resources.humanname import HumanName
from fhir.resources.observation import Observation
import os
from fhirpy import SyncFHIRClient
from apis.env import *

BASE_URL = FHIR_API_URL


def get_FHIR_session():
    _fhir_api_key = INTERSYSTEM_API_KEY
    session = requests.Session()
    session.headers.update({"x-api-key": _fhir_api_key})
    return session


def get_patient_data(patient_id):
    session = get_FHIR_session()
    patient_data_url = f"{BASE_URL}/Patient/{patient_id}"
    response = session.get(patient_data_url)
    patient_response = response.json()
    return patient_response


def insert_patient_data(patient_dict):
    p = Patient()
    name = HumanName()
    name.use = "official"
    name.family = patient_dict["lastName"]
    name.given = [patient_dict['firstName']]
    p.name = [name]
    p.gender = patient_dict["gender"]
    p.birthDate = patient_dict["birthDate"]
    patient_json = p.json()
    post_url = f"{BASE_URL}/Patient"
    session = get_FHIR_session()
    response = session.post(post_url, data=patient_json)
    fhir_id = response.headers['CONTENT-LOCATION'].split("/")[-3]
    return fhir_id

from random import sample
from fhir.resources.patient import Patient
import requests
from fhir.resources.humanname import HumanName
from fhir.resources.observation import Observation
import os
from fhirpy import SyncFHIRClient
from apis.env import *
import copy
import json

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


def get_goal_data(patient_id):
    session = get_FHIR_session()
    patient_data_url = f"{BASE_URL}/Patient/{patient_id}/Goal"
    response = session.get(patient_data_url)
    patient_response = response.json()
    goalsOut = {}
    for it in patient_response["entry"]:
        key = it["resource"]["description"]["text"]
        low_val = it["resource"]["target"][0]["detailRange"]["low"]["value"]
        high_val = it["resource"]["target"][0]["detailRange"]["high"]["value"]
        goalsOut[key] = f'{int(low_val)}-{int(high_val)}' if key != 'bloodOxygen' else f'{int(low_val)}-{high_val}'
    return goalsOut


def insert_goal_data(patient_id, data):
    dataDict = json.loads('{    "resourceType": "Bundle",    "id": "bundle-transaction", "type": "batch",    "entry": [{        "resource": {"resourceType": "Patient", "name": [{"use": "official", "family": "Foo40", "given": ["Bar40"]}],            "gender": "male",            "birthDate": "1974-12-25"            },            "request": {                "method": "POST",                "url": "Patient/14531"            }    },    {        "resource": {            "resourceType": "Observation", "status": "final", "code": {"coding": [{"system": "https://terminology.hl7.org/CodeSystem/observation-category", "code": "activity", "display": "activity"}]}, "subject": {"reference": "Patient/25"}, "effectiveDateTime": "2022-10-15T00:00:00+00:00", "issued": "2022-10-15T22:18:01+00:00", "valueQuantity": {"value": 472.2, "unit": "minutes", "system": "https://unitsofmeasure.org", "code": "minutes"}            },            "request": {                "method": "POST",                "url": "Observation"            }    }]}')
    base_dict = {'resource': {
        "resourceType": "Goal",
        "id": "set goals",
        "lifecycleStatus": "on-hold",
        "subject": {
            "reference": "Patient/"+str(patient_id)
        },
        "target": [
            {
                "measure": {"coding": [{"system": "http://loinc.org", "code": "3141-9"}]},
                "detailRange": {"low": {"value": 0, "unit": ""}, "high": {"value": 0, "unit": ""}}
            }
        ],
    },
        'request': {'method': 'POST', 'url': 'Goal'}}

    bundleEntry = []
    for key in data.keys():
        if key == "sleep":
            units = "hrs"
        elif key == "steps":
            units = "cnt"
        elif key == "heartRate":
            units = "bpm"
        else:
            units = "%"
        sampleDict = copy.deepcopy(base_dict["resource"]["target"][0])
        sampleDict["measure"]["coding"] = [
            {"system": "http://loinc.org", "code": "3141-9"}]
        sampleDict["detailRange"]["low"]["value"] = float(
            data[key].split("-")[0].strip())
        sampleDict["detailRange"]["low"]["unit"] = units
        sampleDict["detailRange"]["high"]["value"] = float(
            data[key].split("-")[-1].strip())
        sampleDict["detailRange"]["high"]["unit"] = units
        base_dict = copy.deepcopy(base_dict)
        base_dict["resource"]["target"] = [sampleDict]
        base_dict["resource"]["description"] = {}
        base_dict["resource"]["description"]["text"] = key
        bundleEntry.append(base_dict)
    dataDict["entry"] = bundleEntry
    session = get_FHIR_session()
    response = session.post(BASE_URL, data=json.dumps(dataDict))
    cnt = 0
    for it in response.json()["entry"]:
        if it["response"]["status"] == "201":
            cnt += 1
    return cnt


def insert_observations(patient_id,data,baseDict):
    dataDict=json.loads('{    "resourceType": "Bundle",    "id": "bundle-transaction", "type": "batch",    "entry": []}')
    bundleEntry=[]
    for it in data:
        baseDict=copy.deepcopy(baseDict)
        baseDict["resource"]["subject"]["reference"]+=str(patient_id)
        baseDict["resource"]["effectiveDateTime"]=it["effectiveDateTime"]
        baseDict["resource"]["issued"]=it["issued"]
        baseDict["resource"]["valueQuantity"]["value"]=it["value"]
        baseDict["resource"]["valueQuantity"]["unit"]=it["unit"]
        baseDict["resource"]["valueQuantity"]["code"]=it["unit"]
        bundleEntry.append(baseDict)
    
    cnt=0
    session = get_FHIR_session()
    def split_list (x):
        return [bundleEntry[i:i+x] for i in range(0, len(bundleEntry), x)]

    for window in split_list(100):
        writeDict=copy.deepcopy(dataDict)
        writeDict["entry"]=window
        post_url = f"{BASE_URL}"
        response = session.post(post_url, data=json.dumps(writeDict))
        if response.json():
            for it in response.json()["entry"]:
                if it["response"]["status"]=="201":
                    cnt+=1
    return cnt
def get_observations(patient_id):
    session = get_FHIR_session()
    observation_url = f"{BASE_URL}/Patient/{patient_id}/Observation"
    response = session.get(observation_url)
    return response.json()


def get_observations_by_url(url):
    session = get_FHIR_session()
    response = session.get(url)
    return response.json()


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

def get_allergy_info(patientId):
    session = get_FHIR_session()
    patient_data_url = f"{BASE_URL}/Patient/{patientId}/AllergyIntolerance"
    response = session.get(patient_data_url)
    patient_response = response.json()
    print(patient_response)
    return patient_response
    

def put_allergy_info(patientId,data):
    #### Pushing Smaple File
    # Sample Json Body for Put Request
    # {
    #     "allergent":"shrimp",
    #     "category":["food"],
    #     "reaction":"Analphytic Reaction"
    # }
    #### can be modified when next version of UI is Made
    dataDict=json.loads(open("../utils/AllergyBundleData_sample.json","r").read())
    dataDict["code"]["coding"][0]["display"]=data["allergent"]
    dataDict["category"]=data["category"]
    dataDict["patient"]["reference"]="Patient/"+str(patientId)
    dataDict["reaction"][0]["description"]=data["reaction"]
    print(json.dumps(dataDict))
    session = get_FHIR_session()
    response = session.post(f"{BASE_URL}/AllergyIntolerance/", data=json.dumps(dataDict))
    print(response)
    # return response.json()
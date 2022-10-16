import pandas as pd
import numpy as np
import os
import random
from tqdm import tqdm
import random
from datetime import datetime, timedelta
import json
import requests
from backend.apis.env import *

BASE_URL = FHIR_API_URL


def get_FHIR_session():
    _fhir_api_key = INTERSYSTEM_API_KEY
    session = requests.Session()
    session.headers.update({"x-api-key": _fhir_api_key})
    return session


data=json.loads('{"resourceType": "Bundle", "id": "bundle-transaction", "type": "batch", "entry": []}')

patientData={'resource': {'resourceType': 'Patient',
    'name': [{'use': 'official', 'family': 'John', 'given': ['Doe']}],
    'gender': 'male',
    'birthDate': '2300-12-12'},
   'request': {'method': 'POST', 'url': 'Patient'}}
observationTimeData={'resource': {'resourceType': 'Observation',
    'status': 'final',
    'code': {'coding': [{'system': 'https://terminology.hl7.org/CodeSystem/observation-category',
       'code': 'activity',
       'display': 'activity'}]},
    'subject': {'reference': 'Patient'},
    'effectiveDateTime': '2022-10-15T00:00:00+00:00',
    'issued': '2022-10-15T22:18:01+00:00',
    'valueQuantity': {'value': 472.2,
     'unit': 'minutes',
     'system': 'https://unitsofmeasure.org',
     'code': 'minutes'}},
   'request': {'method': 'POST', 'url': 'Observation'}}
observationValueData={'resource': {'resourceType': 'Observation',
 'status': 'final',
 'code': {'coding': [{'system': 'https://terminology.hl7.org/CodeSystem/observation-category',
    'code': 'activity',
    'display': 'activity'}]},
 'subject': {'reference': 'Patient'},
 'effectiveDateTime': '2022-10-13T00:00:00+00:00',
 'issued': '2022-10-13T00:00:00+00:00',
 'valueQuantity': {'value': 3228,
  'unit': 'steps',
  'system': 'https://unitsofmeasure.org',
  'code': 'steps'}},
   'request': {'method': 'POST', 'url': 'Observation'}}

bundleEntries=[]
for i in range(1,56):
    patientData=copy.deepcopy(patientData)
    patientData["resource"]["name"][0]["given"]=["Doe"+str(i+1)]
    
    bundleEntries.append(patientData)
import copy
subjlist=list(range(1,56))
for _ in tqdm(subjlist):
    dateLs=pd.date_range('2022-9-15','2022-10-15', freq='D').tolist()
    sleepData=  [np.round(i,2) for i in np.random.uniform(6.5,8.5, len(dateLs))]
    calData=  [np.round(i,2) for i in np.random.uniform(750,2000, len(dateLs))]
    ls=[20,21,22,23]
    sleepStart,sleepEnd=[],[]
    for i in range(len(dateLs)):
        start = dateLs[i]+ timedelta(hours=random.choice(ls))
        end = start + timedelta(hours=2)
        sleepStartTime= start + (end - start) * random.random()
        sleepEndTime = sleepStartTime + timedelta(hours=sleepData[i])
        sleepStart.append(sleepStartTime)
        sleepEnd.append(sleepEndTime)
    dateLs1=pd.date_range('2022-9-15','2022-10-15', freq='400min').tolist()
    spo2Data= [np.round(i,2) for i in np.random.uniform(95,98, len(dateLs1))]
    stressData= [np.round(i,2) for i in np.random.uniform(20,90, len(dateLs1))]
    heartRateData=[np.round(i,2) for i in np.random.uniform(65,180, len(dateLs1))]

    for ts,spo2 in zip([i.strftime("%Y-%m-%dT%H:%M:%S") for i in dateLs1],spo2Data):
        observationValueData=copy.deepcopy(observationValueData)
        observationValueData['resource']['subject']['reference']="Patient/"+str(_)
        observationValueData['resource']['effectiveDateTime']=ts+"+00:00"
        observationValueData['resource']['issued']=ts+"+00:00"
        observationValueData['resource']['valueQuantity']['value']=spo2
        observationValueData['resource']['valueQuantity']['unit']="(%)"
        observationValueData['resource']['valueQuantity']['code']="SpO2"
        bundleEntries.append(observationValueData)
        
    for ts,stress in zip([i.strftime("%Y-%m-%dT%H:%M:%S") for i in dateLs1],stressData):
        observationValueData=copy.deepcopy(observationValueData)
        observationValueData['resource']['subject']['reference']="Patient/"+str(_)
        observationValueData['resource']['effectiveDateTime']=ts+"+00:00"
        observationValueData['resource']['issued']=ts+"+00:00"
        observationValueData['resource']['valueQuantity']['value']=stress
        observationValueData['resource']['valueQuantity']['unit']="(%)"
        observationValueData['resource']['valueQuantity']['code']="Stress"
        bundleEntries.append(observationValueData)
    
    for ts,hr in zip([i.strftime("%Y-%m-%dT%H:%M:%S") for i in dateLs1],heartRateData):
        observationValueData=copy.deepcopy(observationValueData)
        observationValueData['resource']['subject']['reference']="Patient/"+str(_)
        observationValueData['resource']['effectiveDateTime']=ts+"+00:00"
        observationValueData['resource']['issued']=ts+"+00:00"
        observationValueData['resource']['valueQuantity']['value']=hr
        observationValueData['resource']['valueQuantity']['unit']="beats/min"
        observationValueData['resource']['valueQuantity']['code']="HeartRate"
        bundleEntries.append(observationValueData)
    
    for ts,cal in zip([i.strftime("%Y-%m-%dT%H:%M:%S") for i in dateLs],calData):
        observationValueData=copy.deepcopy(observationValueData)
        observationValueData['resource']['subject']['reference']="Patient/"+str(_)
        observationValueData['resource']['effectiveDateTime']=ts+"+00:00"
        observationValueData['resource']['issued']=ts+"+00:00"
        observationValueData['resource']['valueQuantity']['value']=int(cal)
        observationValueData['resource']['valueQuantity']['unit']="kcal"
        observationValueData['resource']['valueQuantity']['code']="Calories Burned"
        bundleEntries.append(observationValueData)
        observationValueData=copy.deepcopy(observationValueData)
        observationValueData['resource']['subject']['reference']="Patient/"+str(_)
        observationValueData['resource']['effectiveDateTime']=ts+"+00:00"
        observationValueData['resource']['issued']=ts+"+00:00"
        observationValueData['resource']['valueQuantity']['value']=3*int(cal)
        observationValueData['resource']['valueQuantity']['unit']="count"
        observationValueData['resource']['valueQuantity']['code']="StepsCount"
        bundleEntries.append(observationValueData)
        
    for ts,ss,sd in zip([i.strftime("%Y-%m-%dT%H:%M:%S") for i in dateLs],[i.strftime("%Y-%m-%dT%H:%M:%S") for i in sleepStart],sleepData):
        observationTimeData=copy.deepcopy(observationTimeData)
        observationTimeData['resource']['subject']['reference']="Patient/"+str(_)
        observationTimeData['resource']['effectiveDateTime']=ts+"+00:00"
        observationTimeData['resource']['issued']=ss+"+00:00"
        observationTimeData['resource']['valueQuantity']['value']=sd*60
        observationTimeData['resource']['valueQuantity']['unit']="mins"
        observationTimeData['resource']['valueQuantity']['code']="Sleep Duration"
        bundleEntries.append(observationTimeData)
 
post_url = f"{BASE_URL}"
session = get_FHIR_session()
def split_list (x):
        return [bundleEntries[i:i+x] for i in range(0, len(bundleEntries), x)]

for window in split_list(100):
    writeDict=copy.deepcopy(data)
    writeDict["entry"]=window
    post_url = f"{BASE_URL}"
    response = session.post(post_url, data=json.dumps(writeDict))

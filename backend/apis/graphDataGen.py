import uuid
from flask_restx import Resource
from flask import request
from marshmallow.exceptions import ValidationError
from apis.database import  get_fhir_id
from apis.fhir_database import insert_observations,get_observations, get_observations_by_url                   
from http import HTTPStatus
from re import sub
import pandas as pd
import numpy as np
from datetime import datetime as dt
def camel_case(s):
  s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
  return ''.join([s[0].lower(), s[1:]])

def get_data_to_list(observations):
    data_list = []
    for entry in observations['entry']:
        resource = entry['resource']
        issued_date = resource['issued']
        effective_date = resource['effectiveDateTime']
        value_quantity = resource['valueQuantity']
        data_list.append({"issued_date": issued_date,
                         "effective_date": effective_date,
                          "value_code": value_quantity["code"],
                          "value": value_quantity["value"]})
    return data_list


def get_next_links(observations, data_list):
    for link in observations["link"]:
        if link["relation"] == "next":
            next_link = link["url"]
            observations = get_observations_by_url(next_link)
            data_list.extend(get_data_to_list(observations))
            return get_next_links(observations, data_list)


class GraphGen(Resource):
    def get(self, id):
        params = request.args.to_dict()
        fhir_id = get_fhir_id(id)
        print(fhir_id)
        observations = get_observations(fhir_id)
        data_list = []
        data_list.extend(get_data_to_list(observations))
        get_next_links(observations, data_list)
        df = pd.DataFrame(data_list)
        print(df.columns)
        df.drop("issued_date",axis=1,inplace=True)
        df.value_code=df.value_code.apply(lambda x:camel_case(x))
        df.effective_date=df.effective_date.apply(lambda x:dt.strptime(x.replace("T"," ").split("+")[0],'%Y-%m-%d %H:%M:%S').timestamp()*1000)
        resutlDict={}
        for value in set(df.value_code):
            df_temp=df[df.value_code==value]
            resutlDict[value]=[[i,j] for i,j in zip(list(df_temp.effective_date),list(df_temp.value))]
        return resutlDict       
       
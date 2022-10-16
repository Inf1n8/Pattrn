import pandas as pd
import numpy as np
from flask_restx import Resource
from flask import request
from marshmallow.exceptions import ValidationError
from apis.database import get_fhir_id
from apis.fhir_database import insert_observations, get_observations, get_observations_by_url
from http import HTTPStatus
from re import sub
import pandas as pd
import numpy as np

baseDict = {'resource': {'resourceType': 'Observation',
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


# def camel_case(s):
#     s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
#     return ''.join([s[0].lower(), s[1:]])


def format_category(cat_type: str) -> str:
    mapping = {'Calories Burned': 'caloriesBurnt', 'HeartRate': 'heartRate',
               'Sleep Duration': 'sleep', 'SpO2': 'bloodOxygen', 'Stress': 'stress', 'steps': 'steps'}
    return mapping[cat_type]


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


class ObservationStats(Resource):
    def get(self, id):
        params = request.args.to_dict()
        if not params.get('window'):
            return {"message": "Missing `window` parameter"}, 400
        fhir_id = get_fhir_id(id)
        observations = get_observations(fhir_id)
        data_list = []
        data_list.extend(get_data_to_list(observations))
        get_next_links(observations, data_list)
        df = pd.DataFrame(data_list)
        df.index = pd.to_datetime(df['effective_date'])
        stats_dict = {}
        df.drop(df[df['value_code'] == 'step'].index, inplace=True)
        for category, category_df in df.groupby('value_code'):
            if category == 'StepsCount':
                continue
            resampled_df = category_df.resample(params["window"])
            average = resampled_df.mean().iloc[-1]
            max_val = resampled_df.max().iloc[-1]
            min_val = resampled_df.min().iloc[-1]
            sum_val = resampled_df.sum().iloc[-1]
            category = format_category(category)
            if category == "bloodOxygen" or category == "stress" or category == "sleep":
                stats_dict[category] = {"value_code": category, "average": np.round(average["value"], 1),
                                        "min": min_val["value"],
                                        "max": max_val["value"], "sum": sum_val["value"]}
            else:
                stats_dict[category] = {"value_code": category, "average": int(average["value"]),
                                        "min": min_val["value"],
                                        "max": max_val["value"], "sum": sum_val["value"]}
        return stats_dict


class Observations(Resource):
    def post(self, id):
        data = request.json
        # List of Dictionaaries where each Dict is of format
        # it={
        #     "effectiveDateTime":"2022-10-13T00:00:00+00:00",
        #     "issued":"2022-10-13T00:00:00+00:00",
        #     "value":3228,
        #     "unit":"steps"
        #     }
        fhir_id = get_fhir_id(id)
        try:
            cnt = insert_observations(fhir_id, data, baseDict)
            return {"message": "Successfully inserted", "numObservations": str(cnt)}, HTTPStatus.ACCEPTED
        except ValidationError as err:
            return {'message': err.messages}, 400

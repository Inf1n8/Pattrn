from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from apis.task import Tasks
from apis.hello import HelloWorld
from apis.login import Login
from apis.patient import PatientDetail, Patients
from apis.goals import GoalDetail
from apis.observations import Observations, ObservationStats
from dotenv import load_dotenv
import os

app = Flask(__name__)
cors = CORS(app, resource={
    r"/*": {
        "origins": "*"
    }
})

api = Api(app, version='1.0', title='TodoMVC API',
          description='A simple TodoMVC API')
api.add_resource(HelloWorld, '/hello')
api.add_resource(Tasks, '/task/<int:id>')
api.add_resource(Login, '/login')
api.add_resource(Patients, '/patients')
api.add_resource(PatientDetail, '/patient_detail/<id>')
# api.add_resource(Goals, '/goal_detail/<id>')
api.add_resource(GoalDetail, '/goal_detail/<id>')
api.add_resource(Observations, '/insert_observations/<id>')
api.add_resource(ObservationStats, '/observation_stats/<id>')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

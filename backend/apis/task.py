from flask_restx import Resource


class Tasks(Resource):
    def get(self, id):
        return {'data': f'Received task id: {id}'}

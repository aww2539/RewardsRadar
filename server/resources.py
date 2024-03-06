from .api import ChaseApi, ChaseListApi
from flask_restful import Api


def create_resources(app):
    api = Api(app, prefix="/api")

    api.add_resource(ChaseApi, "/chase/cards/<string:id>", endpoint='card')
    api.add_resource(ChaseListApi, "/chase/cards", endpoint='cards')

__author__ = 'Ricardo'


def init_rest(flask_app):
    from flask_restful import Api
    api = Api(flask_app, catch_all_404s=True)
    from restful.mocks import MocksAPI
    api.add_resource(MocksAPI, '/v1/mocks')
    return api
from flask_restful import Resource, reqparse


class TestResource(Resource):
    """
    /test/<string:test_id>
    """

    def get(self, test_id):
        return f'successfully tested API {test_id}'

from flask_restful import Resource, reqparse


class FindNthPrimeResource(Resource):
    """
    /test/<string:test_id>
    """

    def get(self, test_id):
        return {
            'success': True,
            'message': f'successfully tested API {test_id}'
        }, 200

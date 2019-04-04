from flask_restful import Resource


class PingResource(Resource):
    """
    /ping
    """

    def get(self):
        return {
            'success': True,
            'message': 'stay woke'
        }

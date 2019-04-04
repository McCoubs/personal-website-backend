from flask_restful import Resource


class PingResource(Resource):
    """
    /wake-up-call
    """

    def get(self):
        return {
            'success': True,
            'message': 'stay woke'
        }

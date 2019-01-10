from flask_restful import Resource, reqparse
from project_euler.find_nth_prime.find_nth_prime import find_nth_prime


class FindNthPrimeResource(Resource):
    """
    /find_nth_prime
    """

    def get(self):
        # parse prime from query params
        nth_prime = reqparse.RequestParser().add_argument('nth_prime', type=int).parse_args().get('nth_prime')
        # process prime
        try:
            result = find_nth_prime(nth_prime)
            output = {
                'success': True,
                'message': f'the {nth_prime} prime number is: {result}',
                'result': result
            }, 200
        except Exception as e:
            output = {
                'success': False,
                'message': str(e)
            }, 400
        return output


class SumSquareDifferenceResource(Resource):
    pass
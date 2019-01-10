from flask_restful import Resource, reqparse
from project_euler import find_nth_prime, sum_square_difference


class FindNthPrimeResource(Resource):
    """
    /find_nth_prime
    """

    def get(self):
        # parse prime from query params
        nth_prime = reqparse.RequestParser().add_argument('value', type=int).parse_args().get('value')
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
    """
    /sum_square_difference
    """

    def get(self):
        # parse value from args
        value = reqparse.RequestParser().add_argument('value', type=int).parse_args().get('value')
        # process sum and square difference
        try:
            result = sum_square_difference(value)
            output = {
                 'success': True,
                 'message': f'the sum square difference of {value} is: {result}',
                 'result': result
             }, 200
        except Exception as e:
            output = {
                 'success': False,
                 'message': str(e)
             }, 400
        return output

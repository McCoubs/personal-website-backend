from flask_restful import Resource, reqparse
from project_euler.find_nth_prime.find_nth_prime import find_nth_prime


class FindNthPrimeResource(Resource):
    """
    /find_nth_prime/<int:nth_prime>
    """

    def get(self, nth_prime):
        return {
            'success': True,
            'message': f'the {nth_prime} prime number is: {find_nth_prime(int(nth_prime))}'
        }, 200

from flask_restful import Resource, reqparse
from project_euler import find_nth_prime, sum_square_difference, largest_continuous_product, largest_prime_factor,\
    pythagorean_triplets


class FindNthPrimeResource(Resource):
    """
    /find_nth_prime
    """

    def get(self):
        # parse prime from query params
        nth_prime = reqparse.RequestParser().add_argument('value', type=int, required=True).parse_args().get('value')
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
        value = reqparse.RequestParser().add_argument('value', type=int, required=True).parse_args().get('value')
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


class LargestContinuousProductResource(Resource):
    """
    /largest_continuous_product
    """

    def get(self):
        # parse series and adjacent values from args
        parser = reqparse.RequestParser()
        args = parser.add_argument('series', type=int, required=True).add_argument('adjacent', type=int, required=True).parse_args()
        series, adjacent = args.get('series'), args.get('adjacent')
        # process largest continuous product
        try:
            result = largest_continuous_product(str(series), adjacent)
            output = {
                 'success': True,
                 'message': f'the largest continuous product of {adjacent} values in given series is: {result}',
                 'result': result
             }, 200
        except Exception as e:
            output = {
                 'success': False,
                 'message': str(e)
             }, 400
        return output


class LargestPrimeFactorResource(Resource):
    """
    /largest_prime_factor
    """

    def get(self):
        # parse value from args
        value = reqparse.RequestParser().add_argument('value', type=int, required=True).parse_args().get('value')
        # process largest prime factor
        try:
            result = largest_prime_factor(value)
            output = {
                 'success': True,
                 'message': f'the largest prime factor of {value} is: {result}',
                 'result': result
             }, 200
        except Exception as e:
            output = {
                 'success': False,
                 'message': str(e)
             }, 400
        return output


class PythagoreanTripletsResource(Resource):
    """
    /pythagorean_triplets
    """

    def get(self):
        # parse value from args
        value = reqparse.RequestParser().add_argument('value', type=int, required=True).parse_args().get('value')
        # process pythagorean triplets
        try:
            result = pythagorean_triplets(value)
            if result is None:
                result = {}
            output = {
                 'success': True,
                 'message': f'the product of the pythagorean triplets of {value} is: {result.get("abc")}',
                 'result': result
             }, 200
        except Exception as e:
            output = {
                 'success': False,
                 'message': str(e)
             }, 400
        return output

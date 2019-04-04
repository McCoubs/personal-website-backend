from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from backend.resources import *


def create_app():
    """Flask application factory. Initializes and returns the Flask application.
    Blueprints are registered in here.
    Modeled after: http://flask.pocoo.org/docs/patterns/appfactories/

    The initialized Flask application.
    """
    # Initialize app. Flatten config_obj to dictionary (resolve properties).
    app = Flask(__name__)
    CORS(app)

    api = Api(app)

    api.add_resource(PingResource, '/ping')
    # project-euler routes
    api.add_resource(FindNthPrimeResource, '/find_nth_prime')
    api.add_resource(SumSquareDifferenceResource, '/sum_square_difference')
    api.add_resource(LargestContinuousProductResource, '/largest_continuous_product')
    api.add_resource(LargestPrimeFactorResource, '/largest_prime_factor')
    api.add_resource(PythagoreanTripletsResource, '/pythagorean_triplets')

    # Return the application instance.
    return app

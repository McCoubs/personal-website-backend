from flask import Flask, request
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

    # Routes
    api.add_resource(TestResource, '/test/<string:test_id>')
    api.add_resource(FindNthPrimeResource, '/find_nth_prime/<int:nth_prime>')

    # Return the application instance.
    return app

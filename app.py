from flask import Flask, jsonify, request
from flask_restful import Api
from backend.resources import *


def create_app():
    """Flask application factory. Initializes and returns the Flask application.
    Blueprints are registered in here.
    Modeled after: http://flask.pocoo.org/docs/patterns/appfactories/

    The initialized Flask application.
    """
    # Initialize app. Flatten config_obj to dictionary (resolve properties).
    app = Flask(__name__)

    api = Api(app)

    # Routes
    api.add_resource(TestResource, '/test', '/test/<string:test_id>')

    # Return the application instance.
    return app

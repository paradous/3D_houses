
from flask import Flask

# App blueprint imports
from src.api.v1 import blueprint


def create_api():

    # Initialize the Flask server
    api = Flask(__name__)

    # Load the blueprints
    api.register_blueprint(blueprint, url_prefix='/v1')

    return api

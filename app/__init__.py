'''intilistaion file for flask app'''
from flask import Flask, jsonify 
from instance.config import app_config


def create_App(config_name):
    '''Configuring the app'''
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('../instance/config.py')

    return app

'''intilistaion file for flask app'''
from flask import Flask
from app.config import app_config


def create_app(config_name):
    '''Configuring the app'''
    app = Flask(__name__)
    app.config.from_object(config.app_config[config_name])
    app.config.from_pyfile('config.py')

    return app

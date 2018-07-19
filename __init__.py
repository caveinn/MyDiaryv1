
from flask import Flask
from flask_restful import Api

from config import app_config
def create_app(config_name):
	app=Flask( __name__ )
	api=Api(app)

	app.config.from_object(app_config[config_name])
from flask import Flask
from .apiv1.config import configuration
from .apiv1 import AppBp as AppBp

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(configuration[config_name])
    app.register_blueprint(AppBp, url_prefix="/api/v1")
    return app
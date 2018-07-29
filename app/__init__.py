from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    from .v_1_0 import app as app_v1_blueprint
    app.register_blueprint(app_v1_blueprint, url_prefix='')

    return app

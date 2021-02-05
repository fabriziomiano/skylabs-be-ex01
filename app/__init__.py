"""
Flask application factory
"""
from jinjasql import JinjaSql
from flask import Flask
from .models import db

jsql = JinjaSql()


def create_app():
    """Application factory"""
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    from app.models import db
    db.init_app(app)

    from app.api import api
    app.register_blueprint(api)

    return app

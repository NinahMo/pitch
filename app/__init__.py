from flask import Flask
from .config import Devconfig
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):

    # Initializing application
    app = Flask(__name__)

    # Setting up configurations
    app.config.from_object(DevConfig)
    app.config.from_pyfile('config.py')


    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    from app import views



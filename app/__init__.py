from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):

    # Initializing application
    app = Flask(__name__)

    app.config.from_object('config')


    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
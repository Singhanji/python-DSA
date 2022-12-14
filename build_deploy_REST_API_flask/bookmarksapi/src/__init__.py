from flask import Flask
import os

from flask_sqlalchemy import SQLAlchemy
from src.auth import auth
from src.bookmarks import bookmarks
from src.omdbapp import omdbapp
from src.home import home
from src.database import db

def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)

    if test_config is None:
        app.config.from_mapping(

            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DB_URI"),
            SQLALCHEMY_TRACK_MODIFICATIONS=False
        )
    else:
        app.config.from_mapping(test_config)

    db.app=app
    db.init_app(app)
    app.register_blueprint(auth)
    app.register_blueprint(bookmarks)
    app.register_blueprint(omdbapp)
    app.register_blueprint(home)

    return app
        
"""   
# Basic application using Flask

    @app.get("/")
    def index():
        return "Hello World"

    @app.get("/hello")
    def hello():
        return {"message":"Hello World"}
"""
    
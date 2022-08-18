from flask import Flask
import os
from src.auth import auth
from src.bookmarks import bookmarks
from src.omdbapp import omdbapp

def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)

    if test_config is None:
        app.config.from_mapping(

            SECRET_KEY=os.environ.get("SECRET_KEY"),
        )
    else:
        app.config.from_mapping(test_config)

    app.register_blueprint(auth)
    app.register_blueprint(bookmarks)
    app.register_blueprint(omdbapp)
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
    
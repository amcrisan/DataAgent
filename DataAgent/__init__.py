from flask import Flask
from flask_cors import CORS

from .config import Config
from . import models, routes

def create_api():
    api = Flask(__name__)
    CORS(api)
    #models.init_app(app)
    api.config.from_object(Config)
    routes.init_app(api)
    return api

# --- Some useful notes ---
#https://lepture.com/en/2018/structure-of-a-flask-project
#https://github.com/hackersandslackers/flask-blueprint-tutorial/tree/master

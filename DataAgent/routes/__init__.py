from flask import Flask
from .home import home_bp

#routes for AI Threads
from .legacy.list_sessions import list_sessions_bp
from .legacy.get_session import get_session_bp

#uploading data
from .uploads.upload_csv import upload_csv_bp #csv data

#Example Data Routes
from .example_data.get_example import get_example_data_bp


def init_app(app: Flask):
    app.register_blueprint(home_bp, url_prefix='/')

    #AI Threads routes
    app.register_blueprint(list_sessions_bp, url_prefix='/legacy')
    app.register_blueprint(get_session_bp,url_prefix='/legacy')

    #Upload Routes
    app.register_blueprint(upload_csv_bp, url_prefix='/upload')


    #Example Data Routes
    app.register_blueprint(get_example_data_bp, url_prefix='/')
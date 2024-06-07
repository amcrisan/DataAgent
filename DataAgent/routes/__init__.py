from flask import Flask
from .home import home_bp

#routes for AI Threads
from .legacy.list_sessions import list_sessions_bp
from .legacy.get_session import get_session_bp


def init_app(app: Flask):
    app.register_blueprint(home_bp, url_prefix='/')

    #AI Threads routes
    app.register_blueprint(list_sessions_bp, url_prefix='/legacy')
    app.register_blueprint(get_session_bp,url_prefix='/legacy')

from flask import Blueprint, current_app
import os
import json

list_sessions_bp = Blueprint('list_sessions', __name__)

@list_sessions_bp.route('/list_sessions')
def list_sessions():
    ''' 
        Assumes that within the top level directory there is
        is a collection of session logs, which are .json files.
        This method will list all the session logs in that
        directory and return a list
    '''
   
    # Accessing the data folder path from the app config
    session_files_dir = current_app.config['SESSION_LOG_DIR']
    try:
        session_files = [f for f in os.listdir(session_files_dir) if f.endswith('.json')]
        return json.dumps(session_files)
    except FileNotFoundError:
        return json.dumps({'error': os.listdir()})
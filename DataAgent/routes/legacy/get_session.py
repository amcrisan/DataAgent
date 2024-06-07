from flask import Blueprint, request, jsonify,current_app
import os
import json

from ...services.legacy.parse_logs import parse_session_logs
from ...services.utils import json_encode

get_session_bp = Blueprint('get_session', __name__)

@get_session_bp.route('/get_session', methods=['GET'])
def get_session():
    '''
        Take the url parameter id and returns the JSON file for a specific session
    '''
    session_id = request.args.get('id')

    session_files_dir = current_app.config['SESSION_LOG_DIR']
    #session_file_path = os.path.join(session_files_dir, session_id, ".json")
    
    try:
        session_messages = parse_session_logs(session_id)
        session_data = [message.__dict__ for message in session_messages]
        return json_encode(session_data)
    
    except FileNotFoundError:
        return jsonify({"error": f"File not Found: {session_files_dir}{session_id}.json" }), 404
    
    except Exception as e:
        return jsonify({"error": f"{str(e)}: {session_files_dir}{session_id}.json" }), 500

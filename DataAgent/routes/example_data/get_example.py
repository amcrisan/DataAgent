from flask import Blueprint, request, current_app, jsonify
import os
import json

get_example_data_bp = Blueprint('get_example_data', __name__)

@get_example_data_bp.route('/get_example_data', methods=['GET'])

def get_example_data():
    data_name = request.args.get('name')
    example_dir = current_app.config['EXAMPLE_DATA_DIR']
    if data_name:
        file_path = os.path.join(example_dir, data_name, data_name + '.json')
        print(f"******File Path: {file_path}")
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            return jsonify(data)
        except FileNotFoundError:
            return jsonify({'error': 'Data file not found'}), 404
    else:
        return jsonify({'error': 'No data name provided'}), 400

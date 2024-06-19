from flask import Blueprint, request, jsonify,current_app
import os
import json

upload_csv_bp = Blueprint('upload_csv_bp',__name__)
@upload_csv_bp.route('/csv', methods=['POST'])
def upload_csv():
    '''
        Uploads a CSV for Data Analysis
    '''

    #Accessing the data upload folder

    upload_csv_dir = current_app.config['UPLOAD_CSV_DIR']

    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No file selected for uploading'}), 400

        if file and file.filename.endswith('.csv'):
            file_path = os.path.join(upload_csv_dir, file.filename)
            file.save(file_path)
            return jsonify({'message': 'File successfully uploaded'}), 201
        else:
            return jsonify({'error': 'Invalid file type. Only CSV files are allowed'}), 400
    else:
        return jsonify({'error': 'Invalid request method. Only POST requests are allowed'}), 405

from flask import Flask, jsonify, render_template, request, flash, redirect
from werkzeug.utils import secure_filename
import os
import pandas as pd
from model import RagModel
from process_entries import process_file 

UPLOAD_FOLDER = '.'
ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model = RagModel()

@app.post("/upload")
def upload_file():
    if 'daylio_csv_file' not in request.files:
        print("File not in requests")
        return "No file was uploaded", 400

    entries_file = request.files['daylio_csv_file']
    
    if entries_file.filename == '':
            print('No selected file')
            return "No file was uploaded", 400
    
    
    if entries_file and allowed_file(entries_file.filename):
        # entries_file.save(os.path.join(app.config['UPLOAD_FOLDER'], "entries_file.csv"))
        print("Start file processing...")
        entries_file = pd.read_csv(entries_file)
            
        model.process_entries(entries=entries_file)
        print("Processing done")
        return "File uploaded successfully", 200 
    
    return "There was an error", 400

@app.post('/ask')
def askQuestion():
    try:
        request_data = request.get_json()
        
        question = request_data['question']
        
        print(f"A question was asked - {question}")
        
        if str(question).strip() == "":
            print("Please enter a valid question")
            return jsonify({"message": "Please enter a valid question"}), 400
        
        response = model.ask_question(question)
        print(f"response - {response}")
        return response, 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return
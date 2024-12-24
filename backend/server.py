from flask import Flask, render_template, request, flash, redirect
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = '.'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.post("/upload")
def upload_file():
    if 'daylio_csv_file' not in request.files:
        print("File not in requests")
        return redirect(request.url)

    print("got file")
    return "File uploaded", 200

@app.route("/home")
def display_dashboard():
    return render_template("../ui/dist/index.html")
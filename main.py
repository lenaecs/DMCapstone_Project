import os
from app import app
from flask import flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import io
import csv

ALLOWED_EXTENSIONS = set(['csv', 'txt'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('//')
def upload_csv_lenae():
    return render_template('upload.html')

reviews = []

@app.route('//', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
            csv_input = csv.reader(stream)
            for line in csv_input:
                reviews.append(line)
            flash('File successfully uploaded')
            return redirect('/')
        else:
            flash('Allowed file types are txt, csv')
            return redirect(request.url)


if __name__ == "__main__":
    app.run()
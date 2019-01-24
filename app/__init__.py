from flask import Flask, request, render_template
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['mp4', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['get'])
def index():
    with open('Object_Number.txt', 'r') as f:
        file = f.readlines()
        lines = [line.rstrip('\n') for line in file]
    return render_template('index.html', tags=lines, index=0)


@app.route('/upload', methods=['post'])
def upload():
    # get choices
    ids = request.form.getlist('choices')

    # create uploaded file container
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    # check if the post request has the file part
    if 'file' not in request.files:
        return index()
    file = request.files['file']

    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        return index()
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        print(app.config['UPLOAD_FOLDER'], filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print()
        # TODO detect
        return index()

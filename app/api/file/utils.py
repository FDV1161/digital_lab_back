import os
from flask import current_app
from werkzeug.utils import secure_filename
from datetime import datetime

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'svg'}


# TODO кидать exception
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def upload_file(file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        hash_value = str(abs(hash(str(datetime) + filename)))
        filename = hash_value + "_" + filename
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        return filename
    return None

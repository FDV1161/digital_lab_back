import os
from flask import request, redirect, url_for, Blueprint, current_app
# from werkzeug import secure_filename
from werkzeug.utils import secure_filename
from datetime import datetime
from app.api.auth import token_auth

bp = Blueprint('file', __name__)


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@bp.route('', methods=['GET', 'POST'])
@token_auth.login_required
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            hash_value = str(abs(hash(str(datetime)+filename)))
            filename = hash_value + "_" + filename
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('uploaded_file', filename=filename))
            return {"file loaded": os.path.join(current_app.config['UPLOAD_FOLDER'], filename)}
    return {"file loaded": "sad"}

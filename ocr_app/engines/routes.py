import os
from flask import render_template, current_app, url_for, flash, redirect, request, Blueprint
from ocr_app.engines.utils import allowed_file, lpr_engine
from werkzeug.utils import secure_filename
from ocr_app.main.routes import main


lpr_model = Blueprint('lpr_model', __name__)
save_location = os.path.join(current_app.root_path, 'static/plate_images')


@lpr_model.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submits an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(save_location, filename))
            # license_number = lpr_engine(os.path.join(save_location, filename))
            # return redirect(url_for('uploaded_file', filename=filename))
            # return redirect(url_for('main.home'))
            flash('File Uploaded Successfully')
        else:
            flash('Invalid File Type')
            return redirect(request.url)
    return redirect(url_for('license_owners.license_plate_recog'))
    # return redirect(url_for('main.home'))

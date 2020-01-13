import os
# from ocr_app.engines.sub_routines import Main
from flask import current_app


allowed_extensions = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions


# def lpr_engine(image_location):
#     return Main(image_location)

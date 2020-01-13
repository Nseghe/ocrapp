import os
from flask import current_app


class Config:
    SECRET_KEY = '695a5d7122facabe9cd3b2fdc6276cd9'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'noreply.algostacks@gmail.com'
    MAIL_PASSWORD = '2569nserah'
    # UPLOAD_FOLDER = os.path.join(current_app.root_path, 'static/plate_images')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
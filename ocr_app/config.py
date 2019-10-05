import os


class Config:
    SECRET_KEY = '695a5d7122facabe9cd3b2fdc6276cd9'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 
    MAIL_PASSWORD = 

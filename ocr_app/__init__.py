from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from ocr_app.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    with app.app_context():
        from ocr_app.users.routes import users
        from ocr_app.main.routes import main
        from ocr_app.license_owners.routes import license_owners
        from ocr_app.customers.routes import customers
        from ocr_app.engines.routes import lpr_model
        from ocr_app.errors.handlers import errors
        app.register_blueprint(users)
        app.register_blueprint(main)
        app.register_blueprint(license_owners)
        app.register_blueprint(customers)
        app.register_blueprint(lpr_model)
        app.register_blueprint(errors)

        return app

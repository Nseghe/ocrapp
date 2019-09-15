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
        # from ocr_app.posts.routes import posts
        from ocr_app.main.routes import main
        from ocr_app.engines.routes import engines
        from ocr_app.customers.routes import customers
        from ocr_app.errors.handlers import errors
        app.register_blueprint(users)
        # app.register_blueprint(posts)
        app.register_blueprint(main)
        app.register_blueprint(engines)
        app.register_blueprint(customers)
        app.register_blueprint(errors)

        return app


# def register_dashapps(app):
#     from ocr_app.dash_apps.layout import layout
#     from ocr_app.dash_apps.callbacks import register_callbacks
#
#     # Meta tags for viewport responsiveness
#     meta_viewport = {"name": "viewport", "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}
#
#     dash_apps = dash.Dash(__name__,
#                           server=app,
#                           url_base_pathname='/customer_page/',
#                           # assets_folder=get_root_path(__name__) + '/assets',
#                           meta_tags=[meta_viewport]
#                           )
#
#     with app.app_context():
#         dash_apps.title = 'Algostacks - Customer Results'
#         dash_apps.layout = layout
#         register_callbacks(dash_apps)
#
# protect_dashviews(dash_apps)

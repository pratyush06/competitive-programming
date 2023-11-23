from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager

login_manager=LoginManager()
login_manager.login_view = 'auth.login'

# The way the application is created in the single-file version is very convenient, but it
# has one big drawback. Because the application is created in the global scope, there is
# no way to apply configuration changes dynamically: by the time the script is running,
# the application instance has already been created, so it is already too late to make
# configuration changes. This is particularly important for unit tests because sometimes
# it is necessary to run the application under different configuration settings for better
# test coverage.
# The solution to this problem is to delay the creation of the application by moving it
# into a factory function

bootstap=Bootstrap() #Flask-Bootstrap packages Bootstrap into an extension that mostly consists of a blueprint named 'bootstrap
mail=Mail()
moment=Moment() #to enhance date formatting with jinja templlaing
db=SQLAlchemy()

def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/main')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    login_manager.init_app(app)
    return app
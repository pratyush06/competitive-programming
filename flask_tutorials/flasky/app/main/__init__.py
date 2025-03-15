# A blueprint is similar to an
# application in that it can also define routes and error handlers. The difference is that
# when these are defined in a blueprint they are in a dormant state until the blueprint is
# registered with an application, at which point they become part of it. Using a blue‐
# print defined in the global scope, the routes and error handlers of the application can
# be defined in almost the same way as in the single-script application.

from flask import Blueprint

main=Blueprint('main', __name__)
login = Blueprint('auth', __name__)
from . import views, errors
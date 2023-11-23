# When users log in to the application, their authenticated state has to be recorded in
# the user session, so that it is remembered as they navigate through different pages.
# Flask-Login is a small but extremely useful extension that specializes in managing
# this particular aspect of a user authentication system, without being tied to a specific
# authentication mechanism.

from flask import Blueprint

auth=Blueprint('auth', __name__)

from . import views
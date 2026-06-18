# This structure has four top-level folders:
# • app/ :The Flask application lives inside a package generically named app.
# • The migrations folder contains the database migration scripts, as before.
# • tests/ :Unit tests are written in a tests package.
# • The venv folder contains the Python virtual environment, as before.
# There are also a few new files:
# • requirements.txt lists the package dependencies so that it is easy to regenerate an
# identical virtual environment on a different computer.
# • config.py stores the configuration settings.
# • flasky.py defines the Flask application instance, and also includes a few tasks that
# help manage the application.

import os
from app import create_app, db
from app.models import User, Role
from flask_migrate import Migrate


app=create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)

@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


# The app.cli.command decorator makes it simple to implement custom commands.
# The name of the decorated function is used as the command name, and the function’s
# docstring is displayed in the help messages. The implementation of the test() func‐
# tion invokes the test runner from the unittest package.

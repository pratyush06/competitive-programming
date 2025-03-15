import unittest
from flask import current_app
from app import create_app, db


# The setUp() method tries to create an environment for the test that is close to that of
# a running application. It first creates an application configured for testing and acti‐
# vates its context. This step ensures that tests have access to current_app , like regular
# requests do. Then it creates a brand-new database for the tests using Flask-
# SQLAlchemy’s create_all() method. The database and the application context are
# removed in the tearDown() method.
# The first test ensures that the application instance exists. The second test ensures that
# the application is running under the testing configuration. To make the tests directory
# a proper package, a tests/init.py module needs to be added, but this can be an empty
# file, as the unittest package scans all the modules to discover the tests.

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    def test_app_exists(self):
        self.assertFalse(current_app is None)
    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
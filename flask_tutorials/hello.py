from flask import Flask

#  All Flask applications must create an application instance. The web server passes all
# requests it receives from clients to this object for handling,

# The only required argument to the Flask class constructor is the name of the main
# module or package of the application. For most applications, Python’s __name__ vari‐
# able is the correct value for this argument.
# Flask uses this argument to determine the location of the applica‐
# tion, which in turn allows it to locate other files that are part of the
# application, such as images and templates.
app=Flask(__name__)

# The Flask application instance needs to know
# what code it needs to run for each URL requested, so it keeps a mapping of URLs to
# Python functions. The association between a URL and the function that handles it is
# called a route.

@app.route('/')
def index():
    return '<hi> Hello world</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hii greeting Mr {}'.format(name)

# Flask also offers a more traditional way to set up the application routes
# with the app.add_url_rule() method, which in its most basic form takes three argu‐
# ments: the URL, the endpoint name, and the view function.

# app.add_url_rule('/', 'index', index)



# Flask applications include a development web server that can be started with the
# flask run command

# ex:- flask --app hello.py run


# The Flask development web server can also be started program‐
# matically by invoking the app.run() method

# if __name__=="__main__":
#     app.run()

# Debug=True
# Flask applications can optionally be executed in debug mode. In this mode, two very
# convenient modules of the development server called the reloader and the debugger
# are enabled by default.
# When the reloader is enabled, Flask watches all the source code files of your project
# and automatically restarts the server when any of the files are modified. Having a
# server running with the reloader enabled is extremely useful during development,
# because every time you modify and save a source file, the server automatically restarts
# and picks up the change.
# The debugger is a web-based tool that appears in your browser when your application
# raises an unhandled exception. The web browser window transforms into an interac‐
# tive stack trace that allows you to inspect source code and evaluate expressions in any
# place in the call stack. You can see how the debugger

# The Request-Response Cycle
# When Flask receives a request from a client, it needs to make a few objects available
# to the view function that will handle it. A good example is the request object, which
# encapsulates the HTTP request sent by the client.
# The obvious way in which Flask could give a view function access to the request
# object is by sending it as an argument, but that would require every single view func‐
# tion in the application to have an extra argument. Things get more complicated if you
# consider that the request object is not the only object that view functions might need
# to access to fulfill a request.
# To avoid cluttering view functions with lots of arguments that may not always be
# needed, Flask uses contexts to temporarily make certain objects globally accessible.
# Thanks to contexts ex:- rquests.context.get('user-agent')

# request dispatching
# When the application receives a request from a client, it needs to find out what view
# function to invoke to service it. For this task, Flask looks up the URL given in the

# request in the application’s URL map, which contains a mapping of URLs to the view
# functions that handle them. Flask builds this map using the data provided in the
# app.route decorator, or the equivalent non-decorator version, app.add_url_rule() .

# request hooks

# Sometimes it is useful to execute code before or after each request is processed. For
# example, at the start of each request it may be necessary to create a database connec‐
# tion or authenticate the user making the request.


# A common pattern to share data between request hook functions and view functions
# is to use the g context global as storage. For example, a before_request handler can
# load the logged-in user from the database and store it in g.user . Later, when the view
# function is invoked, it can retrieve the user from there.

from flask import make_response, render_template
@app.route('/new')
def new_index():
    response=make_response('<h1>index loaded from new index</h1>')
    response.set_cookie('answer', '42')
    return response

# By default Flask looks for templates in a templates subdirectory located inside the
# main application directory

@app.route('/jinja/<name>')
def jinja_engine(name):
    return render_template('user.html', name=name)

## ORM- flask sql alchemy

import os
from flask_sqlalchemy import SQLAlchemy

basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:postgres@localhost/social"

db=SQLAlchemy(app)

class Role(db.Model):
    __tablename__='roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    def __repr__(self):
        return '<Role %r>' % self.name
    
class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    
    def __repr__(self):
        return '<User %r>' % self.username   
    
# Changes to the database are managed through a database session, which Flask-
# SQLAlchemy provides as db.session . To prepare objects to be written to the data‐
# base, they must be added to the session:
    
# The db.create_all() function locates all the subclasses of
# db.Model and creates corresponding tables in the database

# Database sessions are also e.g. db.session.add(), db.session.commit()
# called transactions. 

# filter data Role.query.all(), Role.query.filter_by(name='admin')

# As you make progress developing an application, you will find that your database
# models need to change, and when that happens the database needs to be updated as
# well. Flask-SQLAlchemy creates database tables from models only when they do not
# exist already, so the only way to make it update tables is by destroying the old tables
# first—but of course, this causes all the data in the database to be lost.
# A better solution is to use a database migration framework. In the same way source
# code version control tools keep track of changes to source code files, a database
# migration framework keeps track of changes to a database schema, allowing incre‐
# mental changes to be applied.



#flask migrate
# Flask applications can use the Flask-Migrate
# extension, a lightweight Alembic wrapper that integrates it with the flask command.
from flask_migrate import Migrate

migrate=Migrate(app, db)

# This command creates a migrations directory, where all the migration scripts will be
# stored


# flask db init This command creates a migrations directory, where all the migration scripts will be
# stored

# The flask db migrate subcommand creates an automatic migration script

# Once a migration script has been reviewed and accepted, it can be applied to the data‐
# base using the flask db upgrade command:
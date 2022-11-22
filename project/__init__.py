from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#create app and database instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.sqlite3'
db = SQLAlchemy(app)

#create the tables
from project.models import Client, Book, Log
with app.app_context():
    db.create_all()

#local host and port, exported throughout the program
HOST = 'localhost'
PORT = 5000
HOST_PORT = f'http://{HOST}:{PORT}'

#register blueprints
from project.views.forms import form
from project.views.actions import action

app.register_blueprint(form)
app.register_blueprint(action)










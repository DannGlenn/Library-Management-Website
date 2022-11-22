import json
from flask_sqlalchemy import SQLAlchemy
from project import app
from project.models import Client, Book, Log

#create tables
db = SQLAlchemy(app)
with app.app_context():
    db.create_all()

#load json
with open('populate_db.json', 'r') as fp:
    all_records = json.load(fp)

#populate the tables from loaded json content
with app.app_context():
    for obj in all_records["clients"]:
        client = Client(**obj)
        db.session.add(client)
    for obj in all_records["books"]:
        book = Book(**obj)
        db.session.add(book)
    db.session.commit()
    for obj in all_records["logs"]:
        log = Log(**obj)
        db.session.add(log)
    db.session.commit()
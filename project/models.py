from project import db
import datetime

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    author = db.Column(db.String(20), nullable=False)
    year_published = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Integer, nullable=False)

    def __init__(self, name, author, year_published, type):
        self.name = name
        self.author = author
        self.year_published = year_published
        self.type = type

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __init__(self, name, city, age):
        self.name = name
        self.city = city
        self.age = age

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #referencing foreign key as client_id
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    client_rltnshp = db.relationship('Client', backref='client', lazy=True)
    #referencing foreign key as book_id
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    book_rltnshp = db.relationship('Book', backref='book', lazy=True)
    #additional log details
    borrow_date = db.Column(db.DateTime, nullable=False, default=datetime.date.today())
    return_date = db.Column(db.DateTime, nullable=True, default=None)
    overdue = db.Column(db.Boolean, nullable=False, default=False)


    def __init__(self, client_id, book_id):
        self.client_id = client_id
        self.book_id = book_id

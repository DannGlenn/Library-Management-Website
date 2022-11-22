import datetime
from project import db, HOST_PORT
from flask import Blueprint, render_template, request, redirect
from project.models import Client, Book, Log
from project.views.forms import to_datalist

action = Blueprint('action', __name__, template_folder='templates', url_prefix='/')

#add a new record
@action.route("/<class_name>/", methods=['POST'])
def add_record(class_name):
    #gets parameters from jinja2 form
    attributes = request.form.getlist('attribute')
    #if creating a log, verifiction that client and book exist:
    if class_name == 'log':
        client_exists = False
        book_exists = False
        message = 'Client and Book do not exist!'
        existing_clients = db.session.query(Client).all()
        existing_books = db.session.query(Book).all()
        for client in existing_clients:
            if int(attributes[0]) == client.id:
                client_exists = True
                message = 'Book does not exist!'
                break
        for book in existing_books:
            if int(attributes[1]) == book.id:
                book_exists = True
                message = 'Client does not exist!'
                break
        if (client_exists == False) or (book_exists == False):
            return render_template('new_record.html', adding=class_name, host_port = HOST_PORT, message = message)
    #convert arg class_name, which is passed as string => to Class (includes capitalization and type convertion)
    class_name_to_class = globals()[class_name.capitalize()]
    #constructs an object and adds to db
    new_record = class_name_to_class(*attributes)
    db.session.add(new_record)
    db.session.commit()   
    return render_template('success.html')

#Search record
@action.route("/<class_name>/", methods=['GET'])
def search_record(class_name):
    class_name_to_class = globals()[class_name.capitalize()]
    name = request.args['searchRecordName']
    record = db.session.query(class_name_to_class).filter(class_name_to_class.name==name)
    return render_template('search_record_res.html', records = record[::-1], searching = class_name, host_port = HOST_PORT, name_list = to_datalist(class_name)[::-1])

#Delete record
@action.route("/<class_name>/<int:ind>", methods=['DELETE'])
def delete_record(class_name, ind):
    #an exception is predicted when trying to delete a record already attached to a log
    try:
        class_name_to_class = globals()[class_name.capitalize()]
        record=class_name_to_class.query.get(ind)
        db.session.delete(record)
        db.session.commit()
        return 'ok'
    except:
        return "This record is already attached to a log!"

#display all records
@action.route("/<class_name>/display_all/", methods=['GET'])
def display_all_records(class_name):
    #an 'else' statement not required since every 'if' block ends with a return
    #display all logs
    if class_name == 'log':
        record_array = db.session.query(Log, Client, Book).join(Client, Book).all()
        return render_template('display_logs.html', records = record_array[::-1])
    #display all overdue logs
    if class_name == 'log_overdue':
        record_array = db.session.query(Log, Client, Book).join(Client, Book).filter(Log.overdue == True)
        return render_template('display_logs.html', records = record_array[::-1])
    #display all => other record
    class_name_to_class = globals()[class_name.capitalize()]
    record_array = db.session.query(class_name_to_class).all()
    return render_template('search_record_res.html', records = record_array[::-1], routed_from_display_all=True, searching = class_name, host_port = HOST_PORT)

#update a log return date
@action.route("/<class_name>/<int:ind>/", methods=['PUT'])
def close_log(class_name, ind):
    existing_logs = db.session.query(Log).all()
    for log in existing_logs:
        if ind == log.id:
            if log.return_date == None:
                log = Log.query.get(ind)
                log.return_date = datetime.date.today()
                db.session.commit()
                return 'Log successfully closed!'
            return 'Log already closed!'
    return 'The log ID you entered doesnt exist!'


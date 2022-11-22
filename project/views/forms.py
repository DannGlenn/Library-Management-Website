from flask import Blueprint, render_template
from project import HOST_PORT
from project import db
from project.models import Client, Book, Log

#creating the blueprint
form = Blueprint('form', __name__, template_folder='templates', url_prefix='/form')

#returns a list used in datalist tag when searching a record
def to_datalist(class_name):
    name_list = []
    #specific for logs:
    if class_name == 'log':
        obj_list = db.session.query(Log.id, Client.name, Book.name).join(Client, Book).filter(Log.return_date == None).all()
        return obj_list
    #for all other records beside logs:
    class_name_to_class = globals()[class_name.capitalize()]
    obj_list = db.session.query(class_name_to_class).all()
    for obj in obj_list:
        name_list.append(obj.name)
    return name_list

#routes to forms
@form.route("/add/<class_name>/", methods=['GET'])
def add_record_form(class_name):
    return render_template('new_record.html', adding=class_name, host_port = HOST_PORT)

@form.route("/search/<class_name>/", methods=['GET'])
def search_record_form(class_name):
    return render_template('search_record.html', searching = class_name, host_port = HOST_PORT, 
    name_list=to_datalist(class_name)[::-1])

@form.route("/update/<class_name>/", methods=['GET'])
def update_record_form(class_name):
    return render_template('update_record.html', updating=class_name, host_port = HOST_PORT, 
    id_name_list=to_datalist(class_name))
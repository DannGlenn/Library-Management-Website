from flask import render_template
from project import app, HOST, PORT
from project.scheduler import check_if_overdue


#run on startup
check_if_overdue()

@app.route("/", methods=['GET'])
def home():  
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)


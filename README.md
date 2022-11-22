# Library Management Web App

A management app, meant to be used by librarians  
Was written by Daniel Glencer as an assignment as part of  
'Full stack Python' course, class 7731/12 by John Bryce Training.  

## Installation and Setup

1. Install and create a virtual environment (recommended):  

Install:
```bash
pip install virtualenv
```
Create:
```bash
python -m virtualenv myenv
```
Activate
```bash
.\myenv\Scripts\activate
```
2. Install requirements using the `requirements.txt` file provided:
```bash
pip install -r requirements.txt
```
3. Initiate and populate the database using `init_db.py` (optional, recommended for testing):
```bash
py .\init_db.py
```
4. Run the App:
```bash
py .\app.py
```
## Usage

The App allows the user to:  
  
Add a new client  
Add a new book   
Log a book (when a book is being borrowed)  
Update a log when book is returned   
Display all books   
Display all clients   
Display all logs   
Display late logs   
Find book by name   
Find client by name   
Remove book  
Remover client 

## Technologies used
The program utilizes Python3 as the logic to mediate between the database  
which runs on Sqlite3 and GUI which is written using Jinja2 template engine.  
Flask acting as the main framework, and Sqlalchemy as ORM

## Important Notes
Make sure __port 5000__ isn't being used by another program.  
If it does, simply head over to `/project/__init__.py` and change `PORT = 5000` to whichever port you prefer.  
  
The overdue attribute of logs gets updated every time you run the app, and at 12am while at runtime.
With that being said, looking up overdued logs directly from the database may not produce accurate results  

Searching records is case sensitive. for ease of use, please use the autocomplete suggestions  
  
Additional quality of life improvements such as book quantity, book serial number, and log search  
would be added later on, to avoid deviating from instructed assignment boundaries

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](/LICENSE.txt)
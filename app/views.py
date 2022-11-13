from binascii import Incomplete

from app.form import AssignemntForm
from flask import render_template, flash, request, redirect
from app import app, db, models
import sys

# Route for all assignments
@app.route('/', methods=['GET', 'POST'])
def all():
    with app.app_context():
        assignmentsList = models.Assignment.query.all()
    all={'tag':'all'}
    return render_template('all.html', title='all', all=all, len = len(assignmentsList), assignments = assignmentsList)

# Used for callbacks from '/', '/incomplete'
@app.route('/mark', methods=['POST'])
def mark():
    # JavaScript script will send POST request
    # to this address containing the ID of the 
    # assignment which needs to be marked as complete
    if request.method == 'POST':
        json = request.get_json()
        assign = models.Assignment.query.get(json['value']) # Get Assignemnt by ID
        assign.status = 'complete' # Change 'status' to 'complete'
        db.session.commit() # Save in DB
        return ('', 204) # Respond to JavaScript code with empty response

# Route for complete assignments
@app.route('/complete', methods=['GET', 'POST'])
def complete():
    assignmentsList = getAssignments('complete')
    complete={'tag':'complete'}
    return render_template('complete.html', title='complete', complete=complete, len = len(assignmentsList), assignments = assignmentsList)

# Route for incomplete assignments
@app.route('/incomplete', methods=['GET', 'POST'])
def incomplete(): 
    assignmentsList = getAssignments('incomplete')
    incomplete={'tag':'incomplete'}
    return render_template('incomplete.html', title='incomplete', incomplete=incomplete, len = len(assignmentsList), assignments = assignmentsList)

@app.route('/new', methods=['GET', 'POST'])
def new():
    form = AssignemntForm()
    if form.validate_on_submit():
        p = models.Assignment(status = False, title = form.title.data, notes = form.notes.data, module = form.module.data, date = form.date.data)
        db.session.add(p)
        db.session.commit()
        return redirect("/", code=302)
    return render_template('new.html', title='new', form=form)

# Function for fetching Assignments based on 'status'
def getAssignments(queryParameter):
    with app.app_context():
        assignments = models.Assignment.query.all() # Get all DB entries
    assignmentsList = []
    for i in assignments: 

        # If given Assignment matches given 
        # queryParemeter (complete/incomplete)
        if i.status == queryParameter:
            assignmentsList.append(i) # Add Assignment to return list

    return assignmentsList
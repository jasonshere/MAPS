# import necessary packages
from flask import Blueprint, Flask, render_template, session, redirect, url_for, request, jsonify

# create blueprint object
doctor_blueprint = Blueprint(
    'doctor', 
    __name__,
    url_prefix='/api/v1.0/doctor'
)

@doctor_blueprint.route('/all_patients')
def patients():
    return render_template('doctor/patients.html')

@doctor_blueprint.route('/edit_notes')
def editNotes():
    return render_template('doctor/edit_notes.html')

@doctor_blueprint.route('/edit_diagnoses')
def editDiagnoses():
    return render_template('doctor/edit_diagnoses.html')

@doctor_blueprint.route('/history')
def history():
    return render_template('doctor/history.html')

@doctor_blueprint.route('/set_calendar')
def setCalendar():
    return render_template('doctor/set_calendar.html')

@doctor_blueprint.route('/my_calendar')
def myCalendar():
    return render_template('doctor/my_calendar.html')

@doctor_blueprint.route('/login')
def doctorLogin():
    return render_template('public/login.html')
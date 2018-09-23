# import necessary packages
from flask import Blueprint, Flask, session, redirect, url_for, request, jsonify

# create blueprint object
clerk_blueprint = Blueprint(
    'clerk', 
    __name__,
    url_prefix='/api/v1.0/clerk'
)

@clerk_blueprint.route('/register')
def patientsCalendar():
    return "test"

@clerk_blueprint.route('/doctors_calendar')
def doctorsCalendar():
    return render_template('clerk/doctors_calendar.html', **clerkSetting())

@clerk_blueprint.route('/login')
def clerkLogin():
    return render_template('public/login.html')
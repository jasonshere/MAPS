# import necessary packages
from flask import Blueprint, Flask, render_template, session, redirect, url_for, request, jsonify

# create blueprint object
clerk_blueprint = Blueprint(
    'clerk', 
    __name__,
    template_folder='../../templates',
    url_prefix='/clerk'
)

# setting
def clerkSetting():
    settings = {
        'title' : 'Clerk',
        'menu' : {
            'Patient Appointments' : {
                'icon' : 'mdi mdi-calendar-clock',
                'url': url_for('clerk.patientsCalendar'),
                'new' : True,
            },
            'Doctor Appointments' : {
                'icon' : 'mdi mdi-calendar-clock',
                'url': url_for('clerk.doctorsCalendar'),
                'new' : True,
            }
        }
    }
    return settings

@clerk_blueprint.route('/index')
def index():
    return redirect(url_for('clerk.addDoctor'))

@clerk_blueprint.route('/add_doctor')
def addDoctor():
    return render_template('clerk/add_doctor.html', **clerkSetting())

@clerk_blueprint.route('/patients_calendar')
def patientsCalendar():
    return render_template('clerk/patients_calendar.html', **clerkSetting())

@clerk_blueprint.route('/doctors_calendar')
def doctorsCalendar():
    return render_template('clerk/doctors_calendar.html', **clerkSetting())
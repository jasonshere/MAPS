# import necessary packages
from flask import Blueprint, Flask, render_template, session, redirect, url_for, request, jsonify

# create blueprint object
doctor_blueprint = Blueprint(
    'doctor', 
    __name__,
    template_folder='../../templates',
    url_prefix='/doctor'
)

# setting
def doctorSetting():
    settings = {
        'title' : 'Doctor',
        'menu' : {
            'All scheduled patients': {
                'new' : True,
                'icon' : 'mdi mdi-account',
                'url' : url_for('doctor.patients'),
            },
            'Set Weekly Availability' : {
                'icon' : 'mdi mdi-calendar',
                'url' : url_for('doctor.setCalendar'),
            },
            'My Calendar' : {
                'icon' : 'mdi mdi-calendar',
                'url' : url_for('doctor.myCalendar'),
            }
        }
    }
    return settings

@doctor_blueprint.route('/all_patients')
def patients():
    return render_template('doctor/patients.html', **doctorSetting())

@doctor_blueprint.route('/edit_notes')
def editNotes():
    return render_template('doctor/edit_notes.html', **doctorSetting())

@doctor_blueprint.route('/edit_diagnoses')
def editDiagnoses():
    return render_template('doctor/edit_diagnoses.html', **doctorSetting())

@doctor_blueprint.route('/history')
def history():
    return render_template('doctor/history.html', **doctorSetting())

@doctor_blueprint.route('/set_calendar')
def setCalendar():
    return render_template('doctor/set_calendar.html', **doctorSetting())

@doctor_blueprint.route('/my_calendar')
def myCalendar():
    return render_template('doctor/my_calendar.html', **doctorSetting())

@doctor_blueprint.route('/login')
def doctorLogin():
    return render_template('public/login.html')
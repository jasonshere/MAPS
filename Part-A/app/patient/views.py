# import necessary packages
from flask import Blueprint, Flask, render_template, session, redirect, url_for, request, jsonify

# create blueprint object
patient_blueprint = Blueprint(
    'patient', 
    __name__,
    template_folder='./templates',
    url_prefix='/patient'
)

# setting
def patientSetting():
    settings = {
        'title' : 'Patient',
        'menu' : {
            'Home' : url_for('patient.index'),
            'Appointment' : {
                'Make Appointment' : url_for('patient.makeAppointment'),
                'Delete Appointment' : url_for('patient.deleteAppointment')
            }
        }
    }
    return settings

@patient_blueprint.route('/')
def index():
    return render_template('index.html', **patientSetting())

@patient_blueprint.route('/make_appointment')
def makeAppointment():
    return render_template('calendar.html', **patientSetting())

@patient_blueprint.route('/delete_appointment')
def deleteAppointment():
    return render_template('calendar.html', **patientSetting())
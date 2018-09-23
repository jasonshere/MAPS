# import necessary packages
from flask import Blueprint, Flask, render_template, session, redirect, url_for, request, jsonify

# create blueprint object
patient_blueprint = Blueprint(
    'patient', 
    __name__,
    template_folder='../../templates',
    url_prefix='/patient'
)

# setting
def patientSetting():
    settings = {
        'title' : 'Patient',
        'menu' : {
            'Appointment' : {
                'icon' : 'mdi mdi-calendar-clock',
                'new' : True,
                'children' : {
                    'Make Appointment': url_for('patient.makeAppointment'),
                    'Delete Appointment': url_for('patient.deleteAppointment')
                }
            }
        }
    }
    return settings

@patient_blueprint.route('/make_appointment')
def makeAppointment():
    return render_template('patient/calendar.html', **patientSetting())

@patient_blueprint.route('/delete_appointment')
def deleteAppointment():
    return render_template('patient/calendar.html', **patientSetting())

@patient_blueprint.route('/register')
def register():
    return render_template('patient/register.html', **patientSetting())
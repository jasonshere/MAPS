# import necessary packages
from flask import Blueprint, Flask, render_template, session, redirect, url_for, request, jsonify

# create blueprint object
doctor_blueprint = Blueprint(
    'doctor', 
    __name__,
    template_folder='./templates',
    url_prefix='/doctor'
)

# setting
def doctorSetting():
    settings = {
        'title' : 'Doctor',
        'menu' : {
            'Dashboard' : {
                'url' : url_for('doctor.index'),
                'icon' : 'mdi mdi-elevation-rise'
            },
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

@doctor_blueprint.route('/')
def index():
    return render_template('index.html', **doctorSetting())
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
            'Dashboard' : {
                'url' : url_for('doctor.index'),
                'icon' : 'mdi mdi-elevation-rise'
            },
            'All scheduled patients': {
                'new' : True,
                'icon' : 'mdi mdi-account',
                'url' : url_for('doctor.patients'),
            }
        }
    }
    return settings

@doctor_blueprint.route('/')
def index():
    return render_template('doctor/index.html', **doctorSetting())

@doctor_blueprint.route('/all_patients')
def patients():
    return render_template('doctor/patients.html', **doctorSetting())
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
        'sys_name' : 'Patient Manage',
        'sys_name_agg' : 'PM'
    }
    return settings

@patient_blueprint.route('/')
def patientIndex():
    return render_template('index.html', **patientSetting())
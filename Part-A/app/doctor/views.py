# import necessary packages
from flask import Blueprint, Flask, render_template, session, redirect, url_for, request, jsonify

# create blueprint object
doctor_blueprint = Blueprint(
    'doctor', 
    __name__,
    template_folder='../templates',
    url_prefix='/doctor'
)

# setting
def doctorSetting():
    settings = {
        'sys_name' : 'Doctor Manage',
        'sys_name_agg' : 'DM'
    }
    return settings

@doctor_blueprint.route('/')
def doctorIndex():
    return render_template('index.html', **doctorSetting())
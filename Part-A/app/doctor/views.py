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
        'title' : 'Doctor Manage'
    }
    return settings

@doctor_blueprint.route('/')
def index():
    return render_template('index.html', **doctorSetting())
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
        'sys_name' : 'Clerk Manage',
        'sys_name_agg' : 'CM'
    }
    return settings

@clerk_blueprint.route('/')
def patientIndex():
    return render_template('index.html', **clerkSetting())
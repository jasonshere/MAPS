# import necessary packages
from flask import Blueprint, Flask, render_template, session, redirect, url_for, request, jsonify

# create blueprint object
clerk_blueprint = Blueprint(
    'clerk', 
    __name__,
    template_folder='./templates',
    url_prefix='/clerk'
)

# setting
def clerkSetting():
    settings = {
        'title' : 'Clerk',
        'menu' : {
            'Dashboard' : {
                'url' : url_for('clerk.index'),
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

@clerk_blueprint.route('/')
def index():
    return render_template('index.html', **clerkSetting())
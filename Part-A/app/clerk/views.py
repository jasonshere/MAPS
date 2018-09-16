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
        'title' : 'Clerk',
        'menu' : {
            'Appointment' : {
                'icon' : 'mdi mdi-calendar-clock',
                'url': url_for('clerk.calendar'),
                'new' : True,
            }
        }
    }
    return settings

@clerk_blueprint.route('/')
def index():
    return render_template('clerk/index.html', **clerkSetting())

@clerk_blueprint.route('/calendar')
def calendar():
    return render_template('clerk/calendar.html', **clerkSetting())
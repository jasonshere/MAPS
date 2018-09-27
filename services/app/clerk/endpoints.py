# append path
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))+"/public"))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))+"/doctor"))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

# import necessary packages
from flask import Blueprint, Flask, render_template, session, redirect, url_for, request, jsonify, make_response, session
from init import auth, session
from google_calendar import *
from clerk_models import Clerk
from doctor_models import Doctor
from pub_models import Appointment

# create blueprint object
clerk_blueprint = Blueprint(
    'clerk', 
    __name__,
    url_prefix='/api/v1.0/clerk'
)

# register clerk
@clerk_blueprint.route('/register', methods=["POST"])
@auth.login_required
def register():
    try:
        clerk = Clerk(request.json['clerk'])
        clerk.addClerk()
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Created!'}), 201)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# Clerk login
@clerk_blueprint.route('/login', methods=["POST"])
@auth.login_required
def login():
    try:
        clerk = Clerk(request.json['clerk'])
        res, data = clerk.login()
        if res:
            session['Clerk'] = data
            return make_response(jsonify({'code': 1, 'msg': 'Successfully Signed In!', 'data': data}), 201)
        else:
            return make_response(jsonify({'code': -1, 'msg': 'Username or Password is invalid'}), 400)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# get currently logined clerk
@clerk_blueprint.route('/current', methods=["GET"])
@auth.login_required
def current():
    try:
        data = session['Clerk']
        if data:
            return make_response(jsonify({'code': 1, 'msg': 'Successfully Fetch!', 'data': data}), 201)
        else:
            return make_response(jsonify({'code': -1, 'msg': 'Not Login'}), 400)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': 'Clerk not logged in'}), 400)

# Clerk logout
@clerk_blueprint.route('/logout', methods=["POST"])
@auth.login_required
def logout():
    try:
        session.clear()
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Signed out!'}), 201)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': 'Clerk not logged in'}), 400)

# get all appointments of doctors
@clerk_blueprint.route('/doctors/appointments', methods=["GET"])
def appointmentsOfDoctors():
    try:
        doctor = Doctor({})
        doctors = doctor.getAllDoctors()
        for d in doctors:
            res, appointments = getAppointmentsOfThisWeek(d['calendar_id'])
            if res:
                d["appointments"] = {
                    "count": len(appointments),
                    "data": appointments
                }
            else:
                d["appointments"] = {
                    "count": 0,
                    "data": []
                }
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Fetched!', 'data': doctors}), 201)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)
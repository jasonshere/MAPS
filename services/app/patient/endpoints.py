# append path
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

# import necessary packages
from flask import Blueprint, Flask, render_template, session, redirect, url_for, request, jsonify, make_response, session
from models import Patient
from init import auth, session

# create blueprint object
patient_blueprint = Blueprint(
    'patient', 
    __name__,
    url_prefix='/api/v1.0/patient'
)

@patient_blueprint.route('/register', methods=["POST"])
@auth.login_required
def register():
    try:
        patient = Patient(request.json)
        patient.addPatient()
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Created!'}), 201)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

@patient_blueprint.route('/login', methods=["POST"])
@auth.login_required
def login():
    try:
        patient = Patient(request.json)
        res, data = patient.login()
        if res:
            session['Patient'] = data
            return make_response(jsonify({'code': 1, 'msg': 'Successfully Signed In!'}), 201)
        else:
            return make_response(jsonify({'code': -1, 'msg': 'Username or Password is invalid'}), 400)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

@patient_blueprint.route('/current', methods=["GET"])
@auth.login_required
def current():
    try:
        data = session['Patient']
        if data:
            return make_response(jsonify({'code': 1, 'msg': 'Successfully Fetch!', 'data': data}), 201)
        else:
            return make_response(jsonify({'code': -1, 'msg': 'Not Login'}), 400)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)
        
# append path
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))+"/public"))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

# import necessary packages
from flask import Blueprint, Flask, render_template, session, redirect, url_for, request, jsonify, make_response, session
from models import Patient
from init import auth, session
from google_calendar import *

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
        patient = Patient(request.json['patient'])
        patient.addPatient()
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Created!'}), 201)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

@patient_blueprint.route('/login', methods=["POST"])
@auth.login_required
def login():
    try:
        patient = Patient(request.json['patient'])
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

@patient_blueprint.route('/add_calendar', methods=["POST"])
@auth.login_required
def addCalendar():
    try:
        postData = request.json
        calendarData = postData['calendar']
        
        if calendarData['customer_id'] is None:
            raise Exception('Invalid Parameters')
        
        if calendarData['summary'] is None:
            raise Exception('Invalid Parameters')
        if calendarData['description'] is None:
            raise Exception('Invalid Parameters')
        if calendarData['location'] is None:
            raise Exception('Invalid Parameters')
        if calendarData['timezone'] is None:
            raise Exception('Invalid Parameters')
        
        # get Patient
        patient = Patient({})
        boolean, patientData = patient.getOnePatientById(calendarData['customer_id'])
        if not boolean:
            raise Exception('Patient is not exists')
        else:
            if patientData['calendar_id'] :
                return make_response(jsonify({
                    'code': 1, 
                    'msg': 'Successfully Added!', 
                    'data': {
                        'patient_id': patientData['id'],
                        'calendar_id': patientData['calendar_id'],
                        
                    }
                }), 201)

        res, id = addSecondaryCalendar(calendarData['summary'], calendarData['description'], calendarData['location'], calendarData['timezone'])
        if res:
            # store id to database
            updateData = {
                'calendar_id': id
            }
            patient.updateSchema(patientData['id'], updateData)
            return make_response(jsonify({
                'code': 1, 
                'msg': 'Successfully Added!', 
                'data': {
                    'patient_id': patientData['id'],
                    'calendar_id': id,
                    
                }
            }), 201)
        else:
            raise id
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)
        
# append path
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))+"/doctor"))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))+"/public"))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

# import necessary packages
from flask import Blueprint, Flask, render_template, session, redirect, url_for, request, jsonify, make_response, session
from init import auth, session
from google_calendar import *
from patient_models import Patient
from doctor_models import Doctor
from pub_models import Appointment

# create blueprint object
patient_blueprint = Blueprint(
    'patient', 
    __name__,
    url_prefix='/api/v1.0/patient'
)

# register patient
@patient_blueprint.route('/register', methods=["POST"])
@auth.login_required
def register():
    """
    add a new patient
    :return: json
    """
    try:
        patient = Patient(request.json['patient'])
        patient.addPatient()
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Created!'}), 201)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# Patient login
@patient_blueprint.route('/login', methods=["POST"])
@auth.login_required
def login():
    """
    sign in system as a patient
    :return: json
    """
    try:
        patient = Patient(request.json['patient'])
        res, data = patient.login()
        if res:
            return make_response(jsonify({'code': 1, 'msg': 'Successfully Signed In!', 'data': data}), 201)
        else:
            return make_response(jsonify({'code': -1, 'msg': 'Username or Password is invalid'}), 400)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': 'Patient not logged in'}), 400)

# Patient update
@patient_blueprint.route('/<username>', methods=["PUT"])
@auth.login_required
def update(username):
    """
    update patient by username
    :param username: patient username
    :return: json
    """
    try:
        data = request.json['patient']
        patient = Patient({})
        patient.updateByUsername(username, data)
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Updated!'}), 201)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# list patients
@patient_blueprint.route('/all', methods=["GET"])
@auth.login_required
def getPatients():
    """
    get all patients
    :return: json
    """
    try:
        patient = Patient({})
        results = patient.getAllPatients()
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Fetched!', 'data': results}), 201)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# get specific patient
@patient_blueprint.route('/<patient_id>', methods=["GET"])
@auth.login_required
def getOnePatient(patient_id):
    """
    get one patient
    :param patient_id: patient id
    :return: json
    """
    try:
        patient = Patient({})
        results, data = patient.getOnePatientById(patient_id)
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Fetched!', 'data': data}), 201)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# get patient's google events
@patient_blueprint.route('/calendars/<calendar_id>/events', methods=["GET"])
@auth.login_required
def getEvents(calendar_id):
    """
    get all events by calendar id
    :param calendar_id: calendar id
    :return: json
    """
    try:
        if calendar_id is None:
            raise Exception('Invalid Parameters')
        res, events = getGoogleEvents(calendar_id)
        if res:
            return make_response(jsonify({'code': 1, 'msg': 'Successfully fetched!', 'data': events}), 201)
        else:
            raise events

    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# update patient's google events
@patient_blueprint.route('/calendars/<calendar_id>/events/<event_id>', methods=["PUT"])
@auth.login_required
def updateEvents(calendar_id, event_id):
    """
    update events by calendar id and event id
    :param calendar_id: calendar id
    :param event_id: event id
    :return: json
    """
    try:
        postData = request.json
        eventData = postData['event']
        payload = {
            'summary': eventData['summary'],
            'email': eventData['email'],
            'delete': eventData['delete']
        }
        res, events = updateGoogleEvents(calendar_id, event_id, payload)
        if res:
            return make_response(jsonify({'code': 1, 'msg': 'Successfully fetched!', 'data': events}), 201)
        else:
            raise events

    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# delete patient's google event
@patient_blueprint.route('/calendars/<calendar_id>/events/<event_id>', methods=["DELETE"])
@auth.login_required
def deleteEvent(calendar_id, event_id):
    """
    delete event by calendar id and event id
    :param calendar_id: calendar id and event id
    :param event_id: event id
    :return: json
    """
    try:
        if calendar_id is None:
            raise Exception('Invalid Parameters')
        if event_id is None:
            raise Exception('Invalid Parameters')
        res, e = deleteGoogleEvent(calendar_id, event_id)
        if res:
            return make_response(jsonify({'code': 1, 'msg': 'Successfully deleted!'}), 201)
        else:
            raise e

    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# add appointment
@patient_blueprint.route('/appointments', methods=["POST"])
@auth.login_required
def addAppointments():
    """
    add a appointment
    :return: json
    """
    try:
        postData = request.json['appointment']
        if postData['patient_id'] is None:
            raise Exception('Invalid Parameters')
        if postData['doctor_id'] is None:
            raise Exception('Invalid Parameters')
        if postData['appointed_from'] is None:
            raise Exception('Invalid Parameters')
        if postData['appointed_to'] is None:
            raise Exception('Invalid Parameters')
        if postData['google_calendar_id'] is None:
            raise Exception('Invalid Parameters')
        if postData['google_event_id'] is None:
            raise Exception('Invalid Parameters')

        appointment = Appointment(postData)
        appointment.addAppointment()
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Created!'}), 201)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# get appointments by patient id
@patient_blueprint.route('/<patient_id>/appointments', methods=["GET"])
@auth.login_required
def getAppointments(patient_id):
    """
    get appointments by patient id
    :param patient_id: patient id
    :return: json
    """
    try:
        if patient_id is None:
            raise Exception('Invalid Parameters')

        appointment = Appointment({})
        ds = Doctor({})
        results, data = appointment.getAllAppointmentByPatientId(patient_id, ds)
        if results :
            return make_response(jsonify({'code': 1, 'msg': 'Successfully Fetched!', 'data': data}), 201)
        else:
            raise data
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# delete one appointment
@patient_blueprint.route('/appointments/<event_id>', methods=["DELETE"])
@auth.login_required
def deleteAppointment(event_id):
    """
    delete appointment by event id
    :param event_id: event id
    :return: json
    """
    try:
        appointment = Appointment({})
        appointment.deleteAppointment(event_id)
        return make_response(jsonify({'code': 1, 'msg': 'Successfully deleted!'}), 201)
        
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# append path
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))+"/public"))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

# import necessary packages
from flask import Blueprint, Flask, render_template, session, redirect, url_for, request, jsonify, make_response, session
from init import auth, session
from google_calendar import *
from patient_models import Patient, PatientHistory, Notes, Diagnoses
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
    try:
        patient = Patient({})
        results, data = patient.getOnePatientById(patient_id)
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Fetched!', 'data': data}), 201)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# add patient's calendar
@patient_blueprint.route('/calendars', methods=["POST"])
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
        res, id = addSecondaryCalendar(
            calendarData['summary'], 
            calendarData['description'], 
            calendarData['location'], 
            calendarData['timezone']
        )
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

# add patient's google event
@patient_blueprint.route('/calendars/<calendar_id>/events', methods=["POST"])
@auth.login_required
def addEvents(calendar_id):
    postData = request.json
    eventData = postData['event']     
    
    try:
        if eventData['summary'] is None:
            raise Exception('Invalid Parameters')
        if eventData['description'] is None:
            raise Exception('Invalid Parameters')
        if eventData['location'] is None:
            raise Exception('Invalid Parameters')
        if eventData['timezone'] is None:
            raise Exception('Invalid Parameters')

        if calendar_id is None:
            raise Exception('Invalid Parameters')
        if eventData['start'] is None:
            raise Exception('Invalid Parameters')
        if eventData['end'] is None:
            raise Exception('Invalid Parameters')
        if eventData['patient_email'] is None:
            raise Exception('Invalid Parameters')
        if eventData['doctor_email'] is None:
            raise Exception('Invalid Parameters')

        eventData['start'] = {
            "dateTime": eventData['start'],
            "timeZone": eventData['timezone']
        }
        eventData['end'] = {
            "dateTime": eventData['end'],
            "timeZone": eventData['timezone']
        }
        eventData['calendar_id'] = calendar_id
        res, event = addGoogleEvent(eventData)
        if res:
            return make_response(jsonify({'code': 1, 'msg': 'Successfully added!', 'data': event}), 201)
        else:
            raise event

    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# get patient's google events
@patient_blueprint.route('/calendars/<calendar_id>/events', methods=["GET"])
@auth.login_required
def getEvents(calendar_id):
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

# add history for patient
@patient_blueprint.route('/histories', methods=["POST"])
@auth.login_required
def addHistory():
    try:
        historyData = request.json['history']
        if historyData['patient_id'] is None:
            raise Exception('Invalid Parameters')
        if historyData['doctor_id'] is None:
            raise Exception('Invalid Parameters')
        if historyData['description'] is None:
            raise Exception('Invalid Parameters')
        
        patientHistory = PatientHistory(historyData)
        patientHistory.addHistory()
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Created!'}), 201)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# list history for patient
@patient_blueprint.route('/histories', methods=["GET"])
@auth.login_required
def getHistories():
    try:
        patientHistory = PatientHistory({})
        results = patientHistory.getAllHistory()
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Fetched!', 'data': results}), 201)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# get histories for one patient
@patient_blueprint.route('/<patient_id>/histories', methods=["GET"])
@auth.login_required
def getHistoriesByPatientId(patient_id):
    try:
        patientHistory = PatientHistory({})
        results, data = patientHistory.getAllHistoryByPatientId(patient_id)
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Fetched!', 'data': data}), 201)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# add appointment
@patient_blueprint.route('/appointments', methods=["POST"])
@auth.login_required
def addAppointments():
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

        appointment = Appointment(postData)
        appointment.addAppointment()
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Created!'}), 201)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# get appointments by patient id
@patient_blueprint.route('/<patient_id>/appointments', methods=["GET"])
@auth.login_required
def getAppointments(patient_id):
    try:
        if patient_id is None:
            raise Exception('Invalid Parameters')

        appointment = Appointment({})
        results, data = appointment.getAllAppointmentByPatientId(patient_id)
        if results :
            return make_response(jsonify({'code': 1, 'msg': 'Successfully Fetched!', 'data': data}), 201)
        else:
            raise data
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# get appointments by doctor id
@patient_blueprint.route('/appointments/<doctor_id>', methods=["GET"])
@auth.login_required
def getAppointmentsByDoctorId(doctor_id):
    try:
        if doctor_id is None:
            raise Exception('Invalid Parameters')

        appointment = Appointment({})
        results, data = appointment.getAllAppointmentByDoctorId(doctor_id)
        if results :
            return make_response(jsonify({'code': 1, 'msg': 'Successfully Fetched!', 'data': data}), 201)
        else:
            raise data
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# delete one appointment
@patient_blueprint.route('/appointments/<appointment_id>', methods=["DELETE"])
@auth.login_required
def deleteAppointment(appointment_id):
    try:
        if appointment_id is None:
            raise Exception('Invalid Parameters')
        
        appointment = Appointment({})
        appointment.deleteAppointmentById(appointment_id)
        return make_response(jsonify({'code': 1, 'msg': 'Successfully deleted!'}), 201)
        
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# add one note
@patient_blueprint.route('/notes', methods=["POST"])
@auth.login_required
def addNotes():
    try:
        postData = request.json['note']
        if postData['history_id'] is None:
            raise Exception('Invalid Parameters')
        if postData['patient_id'] is None:
            raise Exception('Invalid Parameters')
        if postData['doctor_id'] is None:
            raise Exception('Invalid Parameters')
        if postData['description'] is None:
            raise Exception('Invalid Parameters')
        if postData['created_at'] is None:
            raise Exception('Invalid Parameters')

        notes = Notes(postData)
        notes.addNote()
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Created!'}), 201)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# get all notes by patient id
@patient_blueprint.route('/<patient_id>/notes', methods=["GET"])
@auth.login_required
def getNotes(patient_id):
    try:
        if patient_id is None:
            raise Exception('Invalid Parameters')

        notes = Notes({})
        results, data = notes.getAllNotesByPatientId(patient_id)
        if results :
            return make_response(jsonify({'code': 1, 'msg': 'Successfully Fetched!', 'data': data}), 201)
        else:
            raise data
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# add diagnose
@patient_blueprint.route('/diagnoses', methods=["POST"])
@auth.login_required
def addDiagnoses():
    try:
        postData = request.json['diagnose']
        if postData['history_id'] is None:
            raise Exception('Invalid Parameters')
        if postData['patient_id'] is None:
            raise Exception('Invalid Parameters')
        if postData['doctor_id'] is None:
            raise Exception('Invalid Parameters')
        if postData['description'] is None:
            raise Exception('Invalid Parameters')
        if postData['created_at'] is None:
            raise Exception('Invalid Parameters')

        diags = Diagnoses(postData)
        diags.addDiagnose()
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Created!'}), 201)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# get all diagnoses by patient id
@patient_blueprint.route('/<patient_id>/diagnoses', methods=["GET"])
@auth.login_required
def getDiagnoses(patient_id):
    try:
        if patient_id is None:
            raise Exception('Invalid Parameters')

        diags = Diagnoses({})
        results, data = diags.getAllDiagnosesByPatientId(patient_id)
        if results :
            return make_response(jsonify({'code': 1, 'msg': 'Successfully Fetched!', 'data': data}), 201)
        else:
            raise Exception('Fetched Failed')
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)
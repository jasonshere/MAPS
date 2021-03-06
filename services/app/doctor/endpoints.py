# append path
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))+"/patient"))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))+"/public"))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

# import necessary packages
from flask import Blueprint, Flask, render_template, session, redirect, url_for, request, jsonify, make_response, session
from init import auth, session
from google_calendar import *
from doctor_models import Doctor
from patient_models import Patient
from pub_models import Appointment

# create blueprint object
doctor_blueprint = Blueprint(
    'doctor', 
    __name__,
    url_prefix='/api/v1.0/doctor'
)

# register doctor
@doctor_blueprint.route('/register', methods=["POST"])
@auth.login_required
def register():
    """
    add a new doctor
    :return: json
    """
    try:
        doctor = Doctor(request.json['doctor'])
        doctor.addDoctor()
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Created!'}), 201)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# Doctor login
@doctor_blueprint.route('/login', methods=["POST"])
@auth.login_required
def login():
    """
    sign in system as a doctor
    :return: json
    """
    try:
        doctor = Doctor(request.json['doctor'])
        res, data = doctor.login()
        if res:
            return make_response(jsonify({'code': 1, 'msg': 'Successfully Signed In!', 'data': data}), 201)
        else:
            return make_response(jsonify({'code': -1, 'msg': 'Username or Password is invalid'}), 400)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# list doctors
@doctor_blueprint.route('/all', methods=["GET"])
@auth.login_required
def getDoctors():
    """
    get all doctors
    :return: json
    """
    try:
        doctor = Doctor({})
        results = doctor.getAllDoctors()
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Fetched!', 'data': results}), 201)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# get specific doctor
@doctor_blueprint.route('/<doctor_id>', methods=["GET"])
@auth.login_required
def getOneDoctor(doctor_id):
    """
    get one doctor
    :param doctor_id: doctor id
    :return: json
    """
    try:
        doctor = Doctor({})
        results, data = doctor.getOneDoctorById(doctor_id)
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Fetched!', 'data': data}), 201)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# add doctor's calendar
@doctor_blueprint.route('/calendars', methods=["POST"])
@auth.login_required
def addCalendar():
    """
    add a calendar for doctor
    :return: json
    """
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
        
        # get Doctor
        doctor = Doctor({})
        boolean, doctorData = doctor.getOneDoctorById(calendarData['customer_id'])
        if not boolean:
            raise Exception('Doctor is not exists')
        else:
            if doctorData['calendar_id'] :
                return make_response(jsonify({
                    'code': 1, 
                    'msg': 'Successfully Added!', 
                    'data': {
                        'doctor_id': doctorData['id'],
                        'calendar_id': doctorData['calendar_id'],
                        
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
            doctor.updateSchema(doctorData['id'], updateData)
            return make_response(jsonify({
                'code': 1, 
                'msg': 'Successfully Added!', 
                'data': {
                    'doctor_id': doctorData['id'],
                    'calendar_id': id,
                    
                }
            }), 201)
        else:
            raise id
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# add doctor's google event
@doctor_blueprint.route('/calendars/<calendar_id>/events', methods=["POST"])
@auth.login_required
def addEvents(calendar_id):
    """
    add event for doctor
    :param calendar_id: calendar id
    :return: json
    """
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

# get doctor's google events
@doctor_blueprint.route('/calendars/<calendar_id>/events', methods=["GET"])
@auth.login_required
def getEvents(calendar_id):
    """
    get all events
    :param calendar_id: calendar_id
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

# delete doctor's google event
@doctor_blueprint.route('/calendars/<calendar_id>/events/<event_id>', methods=["DELETE"])
@auth.login_required
def deleteEvent(calendar_id, event_id):
    """
    delete event by calendar and event id
    :param calendar_id: calendar id
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

# get specific doctor
@doctor_blueprint.route('/email/<doctor_email>', methods=["GET"])
@auth.login_required
def getOneDoctorByEmail(doctor_email):
    """
    get one doctor by email
    :param doctor_email: doctor email
    :return: json
    """
    try:
        doctor = Doctor({})
        results, data = doctor.getOneDoctorByEmail(doctor_email)
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Fetched!', 'data': data}), 201)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# get appointments by doctor id
@doctor_blueprint.route('/<doctor_id>/appointments', methods=["GET"])
@auth.login_required
def getAppointmentsByDoctorId(doctor_id):
    """
    get all appointments by doctor id
    :param doctor_id: doctor id
    :return: json
    """
    try:
        if doctor_id is None:
            raise Exception('Invalid Parameters')
        ps = Patient({})
        appointment = Appointment({})
        results, data = appointment.getAllAppointmentByDoctorId(doctor_id, ps)
        if results :
            return make_response(jsonify({'code': 1, 'msg': 'Successfully Fetched!', 'data': data}), 201)
        else:
            raise data
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# get doctor id by event id
@doctor_blueprint.route('/appointments/event_id/<event_id>', methods=["GET"])
@auth.login_required
def getDoctorIdByEventId(event_id):
    """
    get doctor by event id
    :param event_id: event id
    :return: json
    """
    try:
        if event_id is None:
            raise Exception('Invalid Parameters')
        appointment = Appointment({})
        results, data = appointment.getDoctorIdByEventId(event_id)
        if results :
            return make_response(jsonify({'code': 1, 'msg': 'Successfully Fetched!', 'data': data}), 201)
        else:
            raise data
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# update appointments by id
@doctor_blueprint.route('/appointments/<appointment_id>', methods=["PUT"])
@auth.login_required
def updateAppointmentById(appointment_id):
    """
    update appointment by id
    :param appointment_id: appointment id
    :return: json
    """
    try:
        postData = request.json
        appoData = postData['appointment']  
        if appointment_id is None:
            raise Exception('Invalid Parameters')
        
        appointment = Appointment({})
        appointment.update(appointment_id, appoData)
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Updated!'}), 201)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# get appointments by id
@doctor_blueprint.route('/appointments/<appointment_id>', methods=["GET"])
@auth.login_required
def getAppointmentById(appointment_id):
    """
    get appointment by id
    :param appointment_id: appointment id
    :return: json
    """
    try:
        if appointment_id is None:
            raise Exception('Invalid Parameters')
        appointment = Appointment({})
        results, data = appointment.getAppointmentById(appointment_id)
        if results :
            return make_response(jsonify({'code': 1, 'msg': 'Successfully Fetched!', 'data': data}), 201)
        else:
            raise data
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# get appointments by patient id
@doctor_blueprint.route('/appointments/patient/<patient_id>', methods=["GET"])
@auth.login_required
def getAppointmentsByPatientId(patient_id):
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

# get next patient by doctor id
@doctor_blueprint.route('/<doctor_id>/appointments/next_patient', methods=["GET"])
@auth.login_required
def getNextPatientByDoctorId(doctor_id):
    """
    get next patient by doctor id
    :param doctor_id: doctor id
    :return: json
    """
    try:
        if doctor_id is None:
            raise Exception('Invalid Parameters')
        appointment = Appointment({})
        ps = Patient({})
        results, data = appointment.getNextPatientByDoctorId(doctor_id, ps)
        if results :
            return make_response(jsonify({'code': 1, 'msg': 'Successfully Fetched!', 'data': data}), 201)
        else:
            raise data
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)



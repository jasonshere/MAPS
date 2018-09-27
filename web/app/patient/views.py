# append path
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# import necessary packages
from flask import Blueprint, Flask, render_template, session, redirect, url_for, request, jsonify, make_response
from forms import RegForm, UpdateForm
from app.patient.patient_services import PatientService
from app.doctor.doctor_services import DoctorService
import time
from init import app

# create blueprint object
patient_blueprint = Blueprint(
    'patient', 
    __name__,
    template_folder='../../templates',
    url_prefix='/patient'
)

# setting
def patientSetting():
    settings = {
        'title' : 'Patient',
        'menu' : {
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

@patient_blueprint.route('/index')
def index():
    return redirect(url_for('patient.account'))

@patient_blueprint.route('/account', methods=['GET', 'POST'])
def account():
    form = UpdateForm(request.form)
    if request.method == 'GET':
        form.username.data = session['User']['username']
        form.name.data = session['User']['name']
        form.email.data = session['User']['email']
        form.age.data = session['User']['age']
        form.sex.data = session['User']['sex']
        form.birthday.data = session['User']['birthday']
        form.phone.data = session['User']['phone']
    if request.method == 'POST' and form.validate():
        # update data of patient
        ps = PatientService()
        payload = {
            'patient': form.data
        }
        res, data = ps.update(payload)
        if res:
            return render_template('patient/account.html', **patientSetting(), form = form)
    return render_template('patient/account.html', **patientSetting(), form = form)

# make appointment
@patient_blueprint.route('/make_appointment')
def makeAppointment():
    ds = DoctorService()
    res, doctors = ds.getAll()
    data = doctors['data']
    return render_template('patient/calendar.html', **patientSetting(), doctors=data)

# get doctor
@patient_blueprint.route('/get_doctor/<doctor_id>')
def getDoctor(doctor_id):
    ds = DoctorService()
    res, data = ds.getDoctorById(doctor_id)
    if res:
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Fetched!', 'data': data['data']}), 201)
    else:
        return make_response(jsonify({'code': -1, 'msg': 'Failed'}), 400)

@patient_blueprint.route('/delete_appointment')
def deleteAppointment():
    return render_template('patient/calendar.html', **patientSetting())

# register a patient
@patient_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegForm(request.form)
    if request.method == 'POST' and form.validate():
        # pass the validation, request API
        ps = PatientService()
        payload = {
            'patient' : {
                'username': form.username.data,
                'password': form.password.data,
                'email': form.email.data,
                'created_at': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            }
        }
        res, data = ps.register(payload)
        if res:
            return redirect(url_for('login'))
    return render_template('patient/register.html', form=form)

# get buytime by doctor id
@patient_blueprint.route('/get_busytime/<doctor_id>')
def getBusyTime(doctor_id):
    ds = DoctorService()
    res, data = ds.getBusyTimes(doctor_id)
    events = []
    for field in data['data']:
        events.append({
            'start': field['busytime_from'],
            'end': field['busytime_to'],
            'rendering': 'background',
            'id': field['id']
        })
    if res:
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Fetched!', 'data': events}), 201)
    else:
        return make_response(jsonify({'code': -1, 'msg': 'Failed'}), 400)

# set events
@patient_blueprint.route('/set_events', methods=['POST'])
def setEvents():
    start = request.form.getlist('start')[0]
    end = request.form.getlist('end')[0]
    patient_id = session['User']['id']
    doctor_id = request.form.getlist('doctor_id')[0]
    doctor_email = request.form.getlist('doctor_email')[0]
    patient_email = session['User']['email']

    calendarPayload = {
        "calendar": {
            "summary": "Calendar for Patient",
            "description": "This is Patient Calendar",
            "location": "MAPS",
            "timezone": "Australia/Melbourne",
            "customer_id": patient_id
        }
    }

    ps = PatientService()
    res, data = ps.createCalendar(calendarPayload)
    if res:
        calendarId = data['data']['calendar_id']
        eventPayload = {
            "event": {
                "summary": "Appointment",
                "description": "See the doctor",
                "location": "MAPS",
                "timezone": "Australia/Melbourne",
                "start": start,
                "end": end,
                "patient_email": patient_email,
                "doctor_email": doctor_email
            }
        }
        response, data = ps.createEvent(eventPayload, calendarId)

        if response:
            eventId = data['data']['id']
            payload = {
                "patient_id": patient_id,
                "doctor_id": doctor_id,
                "start": start,
                "end": end,
                "google_event_id": eventId,
                "google_calendar_id": calendarId,
            }
            ret, resp = ps.createEventConnector(payload)
            print(resp)
            return make_response(jsonify({'code': 1, 'msg': 'Successfully Set!', 'data': data['data']}), 201)
        else:
            return make_response(jsonify({'code': -1, 'msg': 'Failed'}), 400)
    return make_response(jsonify({'code': -1, 'msg': 'Failed'}), 400)

# get events
@patient_blueprint.route('/get_events', methods=['GET'])
def getEvents():
    ps = PatientService()
    res, data = ps.getPatientById(session['User']['id'])
    if res:
        calendarId = data['data']['calendar_id']
        ret, events = ps.getAllEvents(calendarId)
        if ret:
            return make_response(jsonify({'code': 1, 'msg': 'Successfully Fetched!', 'data': events['data']}), 201)
        else:
            return make_response(jsonify({'code': -1, 'msg': 'Failed'}), 400)
    return make_response(jsonify({'code': -1, 'msg': data}), 400)

# get events by doctorid
@patient_blueprint.route('/get_events/<doctor_id>', methods=['GET'])
def getEventsByDoctorId(doctor_id):
    ps = PatientService()
    res, data = ps.getEventConnector(doctor_id)
    
    if res:
        calendarId = data['data'][0]['google_calendar_id']
        ret, events = ps.getAllEvents(calendarId)
        print(events)
        if ret:
            return make_response(jsonify({'code': 1, 'msg': 'Successfully Fetched!', 'data': events['data']}), 201)
        else:
            return make_response(jsonify({'code': -1, 'msg': 'Failed'}), 400)
    return make_response(jsonify({'code': -1, 'msg': data}), 400)

# delete event
@patient_blueprint.route('/delete_events', methods=['POST'])
def deleteEvents():
    eventId = request.form.getlist('event_id')[0]
    ps = PatientService()
    calendarId = session['User']['calendar_id']
    res, data = ps.deleteEventById(calendarId, eventId)
    if res:
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Deleted!'}), 201)
    return make_response(jsonify({'code': -1, 'msg': data}), 400)

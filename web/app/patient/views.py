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
                'url' : url_for('patient.makeAppointment'),
            },
            'Account' : {
                'icon' : 'mdi mdi-account',
                'url' : url_for('patient.account'),
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

# get events by doctorid
@patient_blueprint.route('/get_events/<doctor_id>', methods=['GET'])
def getEventsByDoctorId(doctor_id):
    ps = PatientService()
    res, data = ps.getEventsByDoctorId(doctor_id)
    if res and data is not None:
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Fetched!', 'data': data['data']}), 201)
    else:
        return make_response(jsonify({'code': -1, 'msg': 'Failed'}), 201)
    return make_response(jsonify({'code': -1, 'msg': data}), 201)

# get events by doctorid
@patient_blueprint.route('/update_events', methods=['POST'])
def updateEventsByDoctorId():
    doctorId = request.form.getlist('doctor_id')[0]
    eventId = request.form.getlist('event_id')[0]
    delete = request.form.getlist('delete')[0]

    ps = PatientService()
    res, data = ps.updateEventsByDoctorId(doctorId, eventId, session['User']['email'], delete)
    
    if res and data is not None:
        if delete == 'false':
            start = request.form.getlist('start')[0]
            end = request.form.getlist('end')[0]
            patientId = session['User']['id']
            ps.setAppointment(eventId, doctorId, patientId, start, end)
        else:
            ps.deleteAppointment(eventId)
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Updated!'}), 201)
    else:
        return make_response(jsonify({'code': -1, 'msg': 'Failed'}), 201)
    return make_response(jsonify({'code': -1, 'msg': data}), 201)

# delete event
@patient_blueprint.route('/delete_events', methods=['POST'])
def deleteEvents():
    eventId = request.form.getlist('event_id')[0]
    ps = PatientService()
    calendarId = session['User']['calendar_id']
    res, data = ps.deleteEventById(calendarId, eventId)
    if res:
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Deleted!'}), 201)
    return make_response(jsonify({'code': -1, 'msg': data}), 201)

# delete event
@patient_blueprint.route('/get_appointments', methods=['GET'])
def getAppointments():
    patientId = session['User']['id']
    ps = PatientService()
    res, data = ps.getAppointmentsById(patientId)
    if res:
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Get!', 'data': data['data']}), 201)
    return make_response(jsonify({'code': -1, 'msg': data}), 201)



# import necessary packages
from flask import Blueprint, Flask, render_template, session, redirect, url_for, request, jsonify, make_response
from app.doctor.doctor_services import DoctorService
from app.doctor.forms import NoteForm, DiagnoseForm
import json

# create blueprint object
doctor_blueprint = Blueprint(
    'doctor', 
    __name__,
    template_folder='../../templates',
    url_prefix='/doctor'
)

# setting
def doctorSetting():
    """
    menu setting
    :return: menu object
    """
    settings = {
        'title' : 'Doctor',
        'menu' : {
            'All scheduled patients': {
                'new' : True,
                'icon' : 'mdi mdi-account',
                'url' : url_for('doctor.patients'),
            },
            'Set Weekly Availability' : {
                'icon' : 'mdi mdi-calendar',
                'url' : url_for('doctor.setCalendar'),
            }
        }
    }
    return settings

@doctor_blueprint.route('/index')
def index():
    """
    index
    :return: default page
    """
    return redirect(url_for('doctor.setCalendar'))

@doctor_blueprint.route('/all_patients')
def patients():
    """
    get all patients
    :return: render page
    """
    ds = DoctorService()
    doctorId = session['User']['id']
    res, data = ds.getAllPatients(doctorId)    
    return render_template('doctor/patients.html', **doctorSetting(), patients=data['data'])

@doctor_blueprint.route('/edit_notes/<appointment_id>', methods=['GET', 'POST'])
def editNotes(appointment_id):
    """
    edit notes
    :param appointment_id: app id
    :return: render page
    """
    ds = DoctorService()
    form = NoteForm(request.form)
    res, data = ds.getAppointmentById(appointment_id)
    if request.method == 'POST' and form.validate():
        res = ds.editNotes(appointment_id, form.description.data)
    else:
        form.description.data = data['data']['notes']
    return render_template('doctor/edit_notes.html', **doctorSetting(), form=form, address='/doctor/edit_notes/{}'.format(appointment_id))

@doctor_blueprint.route('/edit_diagnoses/<appointment_id>', methods=['GET', 'POST'])
def editDiagnoses(appointment_id):
    """
    edit diagnoses
    :param appointment_id: app id
    :return: render page
    """
    ds = DoctorService()
    form = DiagnoseForm(request.form)
    res, data = ds.getAppointmentById(appointment_id)
    if request.method == 'POST' and form.validate():
        res = ds.editDiags(appointment_id, form.description.data)
    else:
        form.description.data = data['data']['diagnoses']
    return render_template('doctor/edit_diagnoses.html', **doctorSetting(), form=form, address='/doctor/edit_diagnoses/{}'.format(appointment_id))

@doctor_blueprint.route('/history/<patient_id>')
def history(patient_id):
    """
    get all history by patient id
    :param patient_id: patient id
    :return: render page
    """
    ds = DoctorService()
    his, data = ds.getAppointmentsByPatientId(patient_id)
    return render_template('doctor/history.html', **doctorSetting(), history=data['data'])

@doctor_blueprint.route('/set_calendar')
def setCalendar():
    """
    set calendar
    :return: render page
    """
    return render_template('doctor/set_calendar.html', **doctorSetting())

# set free time
@doctor_blueprint.route('/set_free_time', methods=['POST'])
def setFreeTime():
    """
    set free time
    :return: json
    """
    start = request.form.getlist('start')[0]
    end = request.form.getlist('end')[0]
    ds = DoctorService()
    payload = {
        'doctor_email': session['User']['email'],
        'doctor_id': session['User']['id'],
        'start': start,
        'end': end
    }
    res, data = ds.setFreeTime(payload)
    if res:
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Set!', 'data': data['data']}), 201)
    else:
        return make_response(jsonify({'code': -1, 'msg': 'Failed'}), 400)

# get free time
@doctor_blueprint.route('/get_free_time', methods=['GET'])
def getFreeTime():
    """
    get free time
    :return: json
    """
    ds = DoctorService()
    calendarId = session['User']['calendar_id']
    if calendarId is None:
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Get!', 'data': []}), 201)
    
    res, data = ds.getFreeTime(calendarId)
    if res:
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Get!', 'data': data['data']}), 201)
    else:
        return make_response(jsonify({'code': -1, 'msg': 'Failed'}), 400)

# delete free time
@doctor_blueprint.route('/delete_free_time', methods=['POST'])
def deleteFreeTime():
    """
    delete free time
    :return: json
    """
    calendarId = session['User']['calendar_id']
    freeId = request.form.getlist('freeid')[0]
    ds = DoctorService()
    res, data = ds.deleteFreeTime(calendarId, freeId)
    if res:
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Deleted!'}), 201)
    else:
        return make_response(jsonify({'code': -1, 'msg': 'Failed'}), 400)
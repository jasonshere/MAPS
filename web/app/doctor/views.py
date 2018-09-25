# import necessary packages
from flask import Blueprint, Flask, render_template, session, redirect, url_for, request, jsonify, make_response
from app.doctor.doctor_services import DoctorService
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
            },
            'My Calendar' : {
                'icon' : 'mdi mdi-calendar',
                'url' : url_for('doctor.myCalendar'),
            }
        }
    }
    return settings

@doctor_blueprint.route('/index')
def index():
    return redirect(url_for('doctor.setCalendar'))

@doctor_blueprint.route('/all_patients')
def patients():
    return render_template('doctor/patients.html', **doctorSetting())

@doctor_blueprint.route('/edit_notes')
def editNotes():
    return render_template('doctor/edit_notes.html', **doctorSetting())

@doctor_blueprint.route('/edit_diagnoses')
def editDiagnoses():
    return render_template('doctor/edit_diagnoses.html', **doctorSetting())

@doctor_blueprint.route('/history')
def history():
    return render_template('doctor/history.html', **doctorSetting())

@doctor_blueprint.route('/set_calendar')
def setCalendar():
    return render_template('doctor/set_calendar.html', **doctorSetting())

@doctor_blueprint.route('/get_busytime')
def getBusyTime():
    ds = DoctorService()
    res, data = ds.getBusyTimes(session['User']['id'])
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

@doctor_blueprint.route('/my_calendar')
def myCalendar():
    return render_template('doctor/my_calendar.html', **doctorSetting())

# set busy time
@doctor_blueprint.route('/set_busy_time', methods=['POST'])
def setBusyTime():
    start = request.form.getlist('start')[0]
    end = request.form.getlist('end')[0]
    ds = DoctorService()
    payload = {
        'doctor_id': session['User']['id'],
        'start': start,
        'end': end
    }
    res, data = ds.setBusyTime(payload)
    if res:
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Set!', 'data': data}), 201)
    else:
        return make_response(jsonify({'code': -1, 'msg': 'Failed'}), 400)

# delete busy time
@doctor_blueprint.route('/delete_busy_time/<busyid>', methods=['POST'])
def deleteBusyTime(busyid):
    ds = DoctorService()
    res, data = ds.deleteBusyTime(busyid)
    if res:
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Deleted!'}), 201)
    else:
        return make_response(jsonify({'code': -1, 'msg': 'Failed'}), 400)
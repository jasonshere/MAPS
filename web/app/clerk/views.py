# import necessary packages
from flask import Blueprint, Flask, render_template, session, redirect, url_for, request, jsonify, make_response
from app.clerk.forms import AddDoctorForm
from app.doctor.doctor_services import DoctorService
from app.clerk.clerk_services import ClerkService
import time, json

# create blueprint object
clerk_blueprint = Blueprint(
    'clerk', 
    __name__,
    template_folder='../../templates',
    url_prefix='/clerk'
)

# setting
def clerkSetting():
    """
    define menu
    :return: menu object
    """
    settings = {
        'title' : 'Clerk',
        'menu' : {
            'Doctor Appointments' : {
                'icon' : 'mdi mdi-calendar-clock',
                'url': url_for('clerk.doctorsCalendar'),
            },
            'Add Doctor': {
                'icon' : 'mdi mdi-account',
                'url': url_for('clerk.addDoctor'),
            },
            'All Doctors': {
                'icon' : 'mdi mdi-account',
                'url': url_for('clerk.doctorsList'),
            },
            'Statistics': {
                'icon' : 'mdi mdi-chart-bar',
                'url': url_for('clerk.statistics'),
            }
        }
    }
    return settings

@clerk_blueprint.route('/index')
def index():
    """
    index
    :return: default page
    """
    return redirect(url_for('clerk.addDoctor'))

@clerk_blueprint.route('/add_doctor', methods=['GET', 'POST'])
def addDoctor():
    """
    add a doctor
    :return: render page or redirect
    """
    form = AddDoctorForm(request.form)
    if request.method == 'POST' and form.validate():
        # pass the validation, request API
        ds = DoctorService()
        dd = form.data
        dd['created_at'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        payload = {
            'doctor' : dd
        }
        res, data = ds.register(payload)
        
        if res:
            return redirect(url_for('clerk.doctorsList'))
    return render_template('clerk/add_doctor.html', **clerkSetting(), form=form)

@clerk_blueprint.route('/doctors')
def doctorsList():
    """
    get doctor list
    :return:render page
    """
    ds = DoctorService()
    res, doctors = ds.getAll()
    data = doctors['data']
    return render_template('clerk/doctors.html', **clerkSetting(), doctors=data)

@clerk_blueprint.route('/doctors_calendar')
def doctorsCalendar():
    """
    get doctor calendar
    :return: render page
    """
    ds = DoctorService()
    res, doctors = ds.getAll()
    data = doctors['data']
    return render_template('clerk/doctors_calendar.html', **clerkSetting(), doctors=data)

# set free time
@clerk_blueprint.route('/set_free_time/<doctor_id>', methods=['POST'])
def setFreeTime(doctor_id):
    """
    set free time for doctor
    :param doctor_id: doctor id
    :return: json
    """
    start = request.form.getlist('start')[0]
    end = request.form.getlist('end')[0]
    ds = DoctorService()
    res, data = ds.getDoctorById(doctor_id)
    payload = {
        'doctor_email': data['data']['email'],
        'doctor_id': doctor_id,
        'start': start,
        'end': end
    }
    res, data = ds.setFreeTime(payload)
    if res:
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Set!', 'data': data['data']}), 201)
    else:
        return make_response(jsonify({'code': -1, 'msg': 'Failed'}), 400)

# get free time
@clerk_blueprint.route('/get_free_time/<doctor_id>', methods=['GET'])
def getFreeTime(doctor_id):
    """
    get free time
    :param doctor_id: doctor id
    :return: json
    """
    ds = DoctorService()
    res, data = ds.getDoctorById(doctor_id)
    calendarId = data['data']['calendar_id']
    if calendarId is None:
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Get!', 'data': []}), 201)
    
    res, data = ds.getFreeTime(calendarId)
    if res:
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Get!', 'data': data['data']}), 201)
    else:
        return make_response(jsonify({'code': -1, 'msg': 'Failed'}), 400)

# delete free time
@clerk_blueprint.route('/delete_free_time/<doctor_id>', methods=['POST'])
def deleteFreeTime(doctor_id):
    """
    delete free time
    :param doctor_id: doctor id
    :return: json
    """
    ds = DoctorService()
    res, data = ds.getDoctorById(doctor_id)
    calendarId = data['data']['calendar_id']
    freeId = request.form.getlist('freeid')[0]
    
    res, data = ds.deleteFreeTime(calendarId, freeId)
    if res:
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Deleted!'}), 201)
    else:
        return make_response(jsonify({'code': -1, 'msg': 'Failed'}), 400)

# statistics
@clerk_blueprint.route('/statistics', methods=['GET'])
def statistics():
    """
    get statistics
    :return: render page
    """
    return render_template('clerk/statistics.html', **clerkSetting())

# get Json
@clerk_blueprint.route('/statistics/json', methods=['GET'])
def staJson():
    """
    get statistics data
    :return: json
    """
    cs = ClerkService()
    res, data = cs.getStatistics()
    if res:
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Fetched!', "data": data['data']}), 201)
    else:
        return make_response(jsonify({'code': -1, 'msg': 'Failed'}), 400)
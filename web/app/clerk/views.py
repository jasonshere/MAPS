# import necessary packages
from flask import Blueprint, Flask, render_template, session, redirect, url_for, request, jsonify, make_response
from app.clerk.forms import AddDoctorForm
from app.doctor.doctor_services import DoctorService

# create blueprint object
clerk_blueprint = Blueprint(
    'clerk', 
    __name__,
    template_folder='../../templates',
    url_prefix='/clerk'
)

# setting
def clerkSetting():
    settings = {
        'title' : 'Clerk',
        'menu' : {
            'Doctor Appointments' : {
                'icon' : 'mdi mdi-calendar-clock',
                'url': url_for('clerk.doctorsCalendar'),
            },
            'All Doctors': {
                'icon' : 'mdi mdi-account',
                'url': url_for('clerk.doctorsList'),
            }
        }
    }
    return settings

@clerk_blueprint.route('/index')
def index():
    return redirect(url_for('clerk.addDoctor'))

@clerk_blueprint.route('/add_doctor', methods=['GET', 'POST'])
def addDoctor():
    form = AddDoctorForm(request.form)
    if request.method == 'POST' and form.validate():
        # pass the validation, request API
        ds = DoctorService()
        payload = {
            'doctor' : form.data
        }
        res, data = ds.register(payload)
        
        if res:
            return redirect(url_for('clerk.doctorsList'))
    return render_template('clerk/add_doctor.html', **clerkSetting(), form=form)

@clerk_blueprint.route('/doctors')
def doctorsList():
    ds = DoctorService()
    res, doctors = ds.getAll()
    data = doctors['data']
    return render_template('clerk/doctors.html', **clerkSetting(), doctors=data)

@clerk_blueprint.route('/doctors_calendar')
def doctorsCalendar():
    ds = DoctorService()
    res, doctors = ds.getAll()
    data = doctors['data']
    return render_template('clerk/doctors_calendar.html', **clerkSetting(), doctors=data)

# set free time
@clerk_blueprint.route('/set_free_time/<doctor_id>', methods=['POST'])
def setFreeTime(doctor_id):
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
    ds = DoctorService()
    res, data = ds.getDoctorById(doctor_id)
    calendarId = data['data']['calendar_id']
    freeId = request.form.getlist('freeid')[0]
    
    res, data = ds.deleteFreeTime(calendarId, freeId)
    if res:
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Deleted!'}), 201)
    else:
        return make_response(jsonify({'code': -1, 'msg': 'Failed'}), 400)
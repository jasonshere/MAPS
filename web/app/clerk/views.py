# import necessary packages
from flask import Blueprint, Flask, render_template, session, redirect, url_for, request, jsonify
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
            'Patient Appointments' : {
                'icon' : 'mdi mdi-calendar-clock',
                'url': url_for('clerk.patientsCalendar'),
            },
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
            return redirect(url_for('clerk.doctorsList'), **clerkSetting())
    return render_template('clerk/add_doctor.html', **clerkSetting(), form=form)

@clerk_blueprint.route('/doctors')
def doctorsList():
    ds = DoctorService()
    res, doctors = ds.getAll()
    data = doctors['data']
    return render_template('clerk/doctors.html', **clerkSetting(), doctors=data)

@clerk_blueprint.route('/patients_calendar')
def patientsCalendar():
    return render_template('clerk/patients_calendar.html', **clerkSetting())

@clerk_blueprint.route('/doctors_calendar')
def doctorsCalendar():
    return render_template('clerk/doctors_calendar.html', **clerkSetting())
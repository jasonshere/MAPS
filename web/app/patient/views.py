# append path
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# import necessary packages
from flask import Blueprint, Flask, render_template, session, redirect, url_for, request, jsonify
from forms import RegForm, UpdateForm
from app.patient.patient_services import PatientService
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

@patient_blueprint.route('/make_appointment')
def makeAppointment():
    return render_template('patient/calendar.html', **patientSetting())

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
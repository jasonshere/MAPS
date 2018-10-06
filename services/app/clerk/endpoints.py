# append path
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))+"/public"))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))+"/doctor"))
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

# import necessary packages
from flask import Blueprint, Flask, render_template, session, redirect, url_for, request, jsonify, make_response, session
from init import auth, session
from google_calendar import *
from clerk_models import Clerk
from doctor_models import Doctor
from pub_models import Appointment

# create blueprint object
clerk_blueprint = Blueprint(
    'clerk', 
    __name__,
    url_prefix='/api/v1.0/clerk'
)

# register clerk
@clerk_blueprint.route('/register', methods=["POST"])
def register():
    """
    endpoints for adding a new clerk
    :return: json
    """
    try:
        clerk = Clerk(request.json['clerk'])
        clerk.addClerk()
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Created!'}), 201)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)


# Clerk login
@clerk_blueprint.route('/login', methods=["POST"])
@auth.login_required
def login():
    """
    sign in system as clerk
    :return: json
    """
    try:
        clerk = Clerk(request.json['clerk'])
        res, data = clerk.login()
        if res:
            session['Clerk'] = data
            return make_response(jsonify({'code': 1, 'msg': 'Successfully Signed In!', 'data': data}), 201)
        else:
            return make_response(jsonify({'code': -1, 'msg': 'Username or Password is invalid'}), 400)
    except Exception as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)

# get statistics
@clerk_blueprint.route('/statistics', methods=["GET"])
def getAppointmentsGroupByDoctorAndStartDate():
    """
    get statistics data
    :return:  json
    """
    appointment = Appointment()
    doctor = Doctor({})
    data = appointment.getAppointmentsGroupByDoctorAndStartDate()
    for i in range(len(data)):
        for j in range(len(data[i]['appointments'])):
            did = data[i]['appointments'][j]['doctor_id']
            res, da = doctor.getOneDoctorById(did)
            data[i]['appointments'][j]['doctor_name'] = da['name']
    data = assemblyData(data)
    return make_response(jsonify({'code': 1, 'msg': 'Successfully Fetched!', 'data': data}), 201)

# Assembly data
def assemblyData(data):
    """
    assemble data
    :param data: Object
    :return: Object
    """
    # return data
    appoints = {}
    labels = []
    for i in range(len(data)):
        for j in range(len(data[i]['appointments'])):
            label = data[i]['appointments'][j]['doctor_name']
            if label in appoints:
                appoints[label].append(data[i]['appointments'][j]['count'])
            else:
                appoints[label] = [data[i]['appointments'][j]['count']]
        labels.append(data[i]['date'])

    return {'appointments': appoints, 'labels': labels}

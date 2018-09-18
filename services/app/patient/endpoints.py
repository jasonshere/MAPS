# import necessary packages
from flask import Blueprint, Flask, render_template, session, redirect, url_for, request, jsonify, make_response
from sqlalchemy import exc
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from models import Patient

# create blueprint object
patient_blueprint = Blueprint(
    'patient', 
    __name__,
    url_prefix='/api/v1.0/patient'
)

@patient_blueprint.route('/register', methods=["POST"])
def register():
    try:
        new_user = Patient(request.json)
        new_user.addPatient()
        # print(new_user)
        return make_response(jsonify({'code': 1, 'msg': 'Successfully Created!'}), 201)
    except exc.IntegrityError as e:
        return make_response(jsonify({'code': -1, 'msg': str(e)}), 400)
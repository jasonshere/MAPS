# import necessary packages
from flask import Flask, render_template, session, redirect, url_for, request, jsonify, make_response
from app.patient.endpoints import patient_blueprint
from app.doctor.endpoints import doctor_blueprint
from app.clerk.endpoints import clerk_blueprint
import os
from init import app, APIKEY, APIPASS, DEBUG, auth

# create secret key for form to avoid CSRF attack
app.secret_key = os.urandom(32)

# register blueprint
app.register_blueprint(patient_blueprint)
app.register_blueprint(doctor_blueprint)
app.register_blueprint(clerk_blueprint)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/logout')
@auth.login_required
def logout():
    return ''

@auth.get_password
def get_password(username):
    if username == APIKEY:
        return APIPASS
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)

if __name__ == '__main__':
    app.run(debug=DEBUG, host='0.0.0.0', port=8081)
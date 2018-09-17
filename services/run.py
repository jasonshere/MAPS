# import necessary packages
from flask import Flask, render_template, session, redirect, url_for, request, jsonify, make_response
from flask_bootstrap import Bootstrap
from flask_httpauth import HTTPBasicAuth
# from app.patient.views import patient_blueprint
# from app.doctor.views import doctor_blueprint
# from app.clerk.views import clerk_blueprint
import os

# Initialize framework
app = Flask(__name__)
Bootstrap(app)

# create secret key for form to avoid CSRF attack
app.secret_key = os.urandom(32)

auth = HTTPBasicAuth()

# register blueprint
# app.register_blueprint(patient_blueprint, template_folder='templates')
# app.register_blueprint(doctor_blueprint, template_folder='templates')
# app.register_blueprint(clerk_blueprint, template_folder='templates')

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/logout')
@auth.login_required
def logout():
    return ''

@auth.get_password
def get_password(username):
    if username == 'Jason':
        return 'services'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081)
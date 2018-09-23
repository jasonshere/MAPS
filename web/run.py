# import necessary packages
from flask import Flask, render_template, session, redirect, url_for, request, jsonify
from flask_bootstrap import Bootstrap
from app.patient.views import patient_blueprint
from app.doctor.views import doctor_blueprint
from app.clerk.views import clerk_blueprint
import os

# Initialize framework
app = Flask(__name__)
Bootstrap(app)

# create secret key for form to avoid CSRF attack
app.secret_key = os.urandom(32)

# register blueprint
app.register_blueprint(patient_blueprint, template_folder='templates')
app.register_blueprint(doctor_blueprint, template_folder='templates')
app.register_blueprint(clerk_blueprint, template_folder='templates')

@app.route('/logout')
def logout():
    return ''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
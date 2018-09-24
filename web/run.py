# import necessary packages
from flask import Flask, render_template, session, redirect, url_for, request, jsonify
from init import app, DEBUG, PORT
from app.patient.views import patient_blueprint
from app.doctor.views import doctor_blueprint
from app.clerk.views import clerk_blueprint
from app.patient.forms import LoginForm

# register blueprint
app.register_blueprint(patient_blueprint, template_folder='templates')
app.register_blueprint(doctor_blueprint, template_folder='templates')
app.register_blueprint(clerk_blueprint, template_folder='templates')

@app.route('/')
def logout():
    return redirect(url_for('clerkLogin'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        # pass the validation
        return redirect(url_for('patient.makeAppointment'))        
    return render_template('public/login.html', form=form)

if __name__ == '__main__':
    app.run(debug=DEBUG, host='0.0.0.0', port=PORT)
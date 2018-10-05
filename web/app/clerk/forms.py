# import necessary packages
from wtforms import Form, StringField, PasswordField, validators, SelectField
from flask import session
from wtforms.validators import ValidationError
from wtforms.validators import ValidationError
from app.patient.patient_services import PatientService
from app.clerk.clerk_services import ClerkService
from init import session

# define the reg form model
class AddDoctorForm(Form):
    """
    Add doctor form
    """
    username = StringField('Username', validators=[
        validators.DataRequired()
    ])

    sex = SelectField('Sex', choices=[('1', 'Male'), ('2', 'Female')], validators=[
        validators.DataRequired()
    ])

    name = StringField('Name', validators=[
        validators.DataRequired()
    ])

    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])

    confirm = PasswordField('Repeat Password')

    phone = StringField('Phone No', validators=[
        validators.DataRequired()
    ])

    email = StringField('Email', validators=[
        validators.DataRequired()
    ])

    age = StringField('Age', validators=[
        validators.DataRequired()
    ])
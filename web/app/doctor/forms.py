# import necessary packages
from wtforms import Form, StringField, PasswordField, validators, SelectField, TextAreaField
from flask import session
from wtforms.validators import ValidationError
from wtforms.validators import ValidationError
from app.patient.patient_services import PatientService
from app.clerk.clerk_services import ClerkService
from app.doctor.doctor_services import DoctorService
from init import session

# define the notes form model
class NoteForm(Form):
    description = TextAreaField('Description', validators=[
        validators.DataRequired(),
    ])

# define the diagnoses form model
class DiagnoseForm(Form):
    description = TextAreaField('Description', validators=[
        validators.DataRequired(),
    ])


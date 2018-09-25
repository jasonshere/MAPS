# import necessary packages
from wtforms import Form, StringField, PasswordField, validators, SelectField
from flask import session
from wtforms.validators import ValidationError
from wtforms.validators import ValidationError
from patient_services import PatientService
from clerk_services import ClerkService
from init import session

# define the reg form model
class RegForm(Form):
    username = StringField('username', validators=[
        validators.DataRequired(),
        validators.Length(min=4, max=25)
    ])

    email = StringField('email', validators=[
        validators.DataRequired(),
        validators.Email()
    ])

    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])

    confirm = PasswordField('Repeat Password')

# define the login form model
class LoginForm(Form):
    username = StringField('username', validators=[
        validators.DataRequired()
    ])

    password = PasswordField('password', validators=[
        validators.DataRequired()
    ])

    role = SelectField('role', choices=[('1', 'Patient'), ('2', 'Doctor'), ('3', 'Clerk')], validators=[
        validators.DataRequired()
    ])

    # validate username and password
    def validate_username(form, field):
        username = field.data
        password = form.password.data
        role = form.role.data
        if role == '1':
            ps = PatientService()
            payload = {
                'patient': {
                    'username': username,
                    'password': password
                }
            }
            res, data = ps.login(payload)
            
            if res is False:
                raise ValidationError('Username Or Password Is Invalid')
            else:
                d = data['data']
                d['type'] = 'Patient'
                session['User'] = d
        elif role == '3':
            cs = ClerkService()
            payload = {
                'clerk': {
                    'username': username,
                    'password': password
                }
            }
            res, data = cs.login(payload)
            
            if res is False:
                raise ValidationError('Username Or Password Is Invalid')
            else:
                d = data['data']
                d['type'] = 'Patient'
                session['User'] = d

# define form for account
class UpdateForm(Form):
    username = StringField('Username', validators=[
        validators.DataRequired()
    ])

    sex = SelectField('Sex', choices=[('1', 'Male'), ('2', 'Female')], validators=[
        validators.DataRequired()
    ])

    name = StringField('Name', validators=[
        validators.DataRequired()
    ])

    birthday = StringField('Birthday', validators=[
        validators.DataRequired()
    ])

    phone = StringField('Phone No', validators=[
        validators.DataRequired()
    ])

    email = StringField('Email', validators=[
        validators.DataRequired()
    ])

    age = StringField('Age', validators=[
        validators.DataRequired()
    ])
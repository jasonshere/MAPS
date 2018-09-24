# import necessary packages
from wtforms import Form, StringField, PasswordField, validators, SelectField
from wtforms.validators import ValidationError
from wtforms.validators import ValidationError
from services import PatientService

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
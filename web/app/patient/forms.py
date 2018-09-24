# import necessary packages
from wtforms import Form, StringField, PasswordField, validators, SelectField
from wtforms.validators import ValidationError

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
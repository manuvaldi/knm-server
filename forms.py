from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectMultipleField
from wtforms.validators import DataRequired, Email, Length, NumberRange


class NetworkForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=-1, max=80, message='You cannot have more than 80 characters')])
    cidr = StringField('CIDR', validators=[DataRequired(),Length(min=-1, max=100, message='You cannot have more than 100 characters')])
    vlanid = IntegerField('VLAN ID', validators=[DataRequired(), NumberRange(min=1, max=1500, message='VLAN ID must be between 1-1500')])
    options = StringField('Options', validators=[Length(min=-1, max=4, message='You cannot have more than 4 characters')])
    servers = SelectMultipleField('Servers')

class ServerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=-1, max=80, message='You cannot have more than 80 characters')])
    description = StringField('Description', validators=[DataRequired(),Length(min=-1, max=100, message='You cannot have more than 100 characters')])
    mac_address = StringField('MAC Address', validators=[Length(min=-1, max=18, message='You cannot have more than 18 characters')])

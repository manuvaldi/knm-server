from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, Length


class NetworkForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=-1, max=80, message='You cannot have more than 80 characters')])
    cidr = StringField('CIDR', validators=[DataRequired(),Length(min=-1, max=100, message='You cannot have more than 100 characters')])
    servers = StringField('Servers', validators=[DataRequired(), Length(min=-1, max=200, message='You cannot have more than 200 characters')])
    vlanid = StringField('VLAN ID', validators=[DataRequired(), Length(min=-1, max=20, message='You cannot have more than 20 characters')])
    options = StringField('Options', validators=[Length(min=-1, max=4, message='You cannot have more than 4 characters')])

from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, StringField
from wtforms.validators import DataRequired, NumberRange, InputRequired, Regexp


class InsertDataForm(FlaskForm):
    numbers = StringField(label='numbers', validators=[DataRequired(), Regexp(r'((\d)+\s)*(\d+)', message='please only insert numbers!')])
    k = IntegerField(label='number of bins', validators=[DataRequired(message='number of bins must be >= 1'), NumberRange(1, 10)])
    submit = SubmitField(label='calculate')


class ReturnButton(FlaskForm):
    button = SubmitField(label='Return To Main Page')

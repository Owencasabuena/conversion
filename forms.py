from flask_wtf import FlaskForm
from wtforms import DecimalField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired

class conversionForm(FlaskForm):
    convert_temperature = SubmitField("Convert Temperature")
    convert_measurement = SubmitField("Convert Measurement")

class measurementForm(FlaskForm):
    value = DecimalField('Enter Value', validators=[DataRequired()])
    metric_from = SelectField(
        'From',
        choices=[
            ('km', 'kilometers (km)'),
            ('m', 'meters (m)'),
            ('cm', 'centimeters (cm)'),
            ('mm', 'millimeters (mm)')
        ],
        validators=[DataRequired()]
    )
    metric_to = SelectField(
        'To',
        choices=[
            ('km', 'kilometers (km)'),
            ('m', 'meters (m)'),
            ('cm', 'centimeters (cm)'),
            ('mm', 'millimeters (mm)')
        ],
        validators=[DataRequired()]
    )
    submit = SubmitField('Convert')

class temperatureForm(FlaskForm):
    value = FloatField('Enter Value', validators=[DataRequired()])
    temp_from = SelectField(
        'From',
        choices=[
            ('C', 'Celcius'),
            ('F', 'Fahrenheit'),
            ('K', 'Kelvin')
        ],
        validators=[DataRequired()]
    )
    temp_to = SelectField(
        'To',
        choices=[
            ('C', 'Celcius'),
            ('F', 'Fahrenheit'),
            ('K', 'Kelvin')
        ],
        validators=[DataRequired()]
    )
    submit = SubmitField('Convert')
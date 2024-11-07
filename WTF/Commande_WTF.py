from flask_wtf import FlaskForm  # FlaskForm is the recommended class instead of Form
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError
from wtforms.validators import DataRequired, NumberRange

class CommandeForm(FlaskForm):  # FlaskForm should be inherited instead of Form
    client_id = IntegerField('Client ID', validators=[DataRequired()])
    product_id = IntegerField('Product ID', validators=[DataRequired()])
    qte = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1, message="Quantity must be at least 1")])
    submit = SubmitField('Place Order')

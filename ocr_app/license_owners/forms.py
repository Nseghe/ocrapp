from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from wtforms.validators import DataRequired, Length


class CustomerForm(FlaskForm):
    customerid = StringField('Customer ID', validators=[DataRequired(), Length(min=10, max=10)])
    customername = StringField('Customer Name', validators=[DataRequired()])
    accountno = StringField('Account No.', validators=[DataRequired()])
    accounttype = RadioField('Account Type', choices=[('savings', 'Savings'), ('current', 'Current')])
    submit = SubmitField('Predict Loan Default')

class LicensePlateForm(FlaskForm):
    plate_number = StringField('License Plate Number',
                           validators=[DataRequired(), Length(min=3, max=9)])
    submit = SubmitField('Search Database')

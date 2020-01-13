from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired, Length, ValidationError
from ocr_app.models import License_Owner


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

    def validate_plate_number(self, plate_number):
        license_owner = License_Owner.query.filter_by(license_number=plate_number.data).first()
        if len(plate_number.data)>2 and len(plate_number.data)<10:
            if not license_owner:
                raise ValidationError('That License Number does not exist in our database. Please try again.')


class LicensePlateImageForm(FlaskForm):
    plate_image = FileField('License Plate Image', validators=[FileRequired()])
    submit = SubmitField('Upload Image')

    def allowed_file(filename):
        allowed_extensions = set(['jpg', 'jpeg'])
        if not ('.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions):
            raise ValidationError("This file type is not Valid. \nPlease select a 'jpg' or 'jpeg' file")
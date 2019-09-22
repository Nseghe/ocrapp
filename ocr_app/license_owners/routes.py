from flask import render_template, redirect, url_for, Blueprint
from flask_login import login_required
from ocr_app.license_owners.forms import LicensePlateForm
from ocr_app.models import License_Owners

license_owners = Blueprint('license_owners', __name__)


@license_owners.route("/license_plate_recognition", methods=['GET', 'POST'])
@login_required
def license_plate_recognition():
	form = LicensePlateForm()
	if form.validate_on_submit():
		return redirect(url_for('license_owners.license_owner'))
	return render_template('license_plate_recognition.html', title='License Plate Recognition', form=form)


@license_owners.route("/license_owner", methods=['POST', 'GET'])
@login_required
def license_owner():
	# id = int(request.form["id"])
	license_owner = License_Owners.query.get(1)
	# #present_customer.age = present_customer.age  # type: object
	return render_template('license_owner.html', title='License Owner', license_owner=license_owner)

from flask import render_template, redirect, request, url_for, Blueprint
from flask_login import login_required
from ocr_app.license_owners.forms import LicensePlateForm
from ocr_app.models import License_Owner

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
	license_owner = License_Owner.query.get('AAA841LE')
	# #present_customer.age = present_customer.age  # type: object
	return render_template('license_owner.html', title='License Owner', license_owner=license_owner)


@license_owners.route("/show_all_license_owners", methods=['GET', 'POST'])
@login_required
def show_all_license_owners():
    page = request.args.get('page', 1, type=int)
    all_license_owners = License_Owner.query.order_by(License_Owner.id.desc()).paginate(page=page, per_page=50)
    return render_template('show_all_license_owners.html', title='All Customers', all_license_owners=all_license_owners)

from flask import render_template, redirect, request, flash, url_for, Blueprint
from flask_login import login_required
from ocr_app.license_owners.forms import LicensePlateForm
from ocr_app.models import License_Owner
from ocr_app.main.routes import main

license_owners = Blueprint('license_owners', __name__)


@license_owners.route("/license_plate_recog", methods=['GET', 'POST'])
@login_required
def license_plate_recog():
	form = LicensePlateForm()
	if form.validate_on_submit():
		# flash(form.plate_number.data)
		return redirect(url_for('license_owners.license_owner', plate_number=form.plate_number.data))
	return render_template('license_plate_recog.html', title='License Plate Recognition', form=form)


@license_owners.route("/license_owner", methods=['GET', 'POST'])
@login_required
def license_owner():
	plate_number = request.args.get('plate_number', None)
	license_own = License_Owner.query.get(plate_number)
	flash(license_own)
	return render_template('temp_license_owner.html', title='License Owner', license_own=license_own)


@license_owners.route("/show_all_license_owners", methods=['GET', 'POST'])
@login_required
def show_all_license_owners():
    # page = request.args.get('page', 1, type=int)
    # all_license_owners = License_Owner.query.order_by(License_Owner.license_number.desc()).paginate(page=page, per_page=100)
    # return render_template('show_all_license_owners.html', title='All License Owners', all_license_owners=all_license_owners)
	return redirect(url_for('main.testing', temp='AMD2346HG'))

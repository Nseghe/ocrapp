from flask import (render_template, request, Blueprint)
from flask_login import login_required
from ocr_app.models import Customer

engines = Blueprint('engines', __name__)


@engines.route("/license_plate_recognition", methods=['GET', 'POST'])
@login_required
def license_plate_recognition():
	return render_template('license_plate_recognition.html', title='License Plate Recognition')

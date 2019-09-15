from datetime import datetime
from ocr_app import db
from flask import (render_template, request, redirect, Blueprint)
from ocr_app.engines.forms import CustomerForm
from flask_login import login_required
from ocr_app.models import Customer


customers = Blueprint('customers', __name__)


@customers.route("/new_customer", methods=['GET', 'POST'])
@login_required
def show_models():
    form = CustomerForm()
    return render_template('new_customer.html', title='New Customer', form=form)


@customers.route("/show_all_customers", methods=['GET', 'POST'])
@login_required
def show_all_customers():
    page = request.args.get('page', 1, type=int)
    all_customers = Customer.query.order_by(Customer.id.desc()).paginate(page=page, per_page=100)
    return render_template('show_all_customers.html', title='All Customers', all_customers=all_customers)


@customers.route("/add_new_customer", methods=['GET', 'POST'])
@login_required
def add_new_customer():
    page = request.args.get('page', 1, type=int)
    all_customers = Customer.query.order_by(Customer.id.desc()).paginate(page=page, per_page=7)
    return render_template('add_new_customer.html', title='New Customer', all_customers=all_customers)


@customers.route("/update_customer_data/<int:id>", methods=['GET', 'POST'])
@login_required
def update_customer_data(id):
    if request.method == "POST":
        age = request.form["flight"]
        job = request.form["destination"]
        marital_status = datetime.strptime(request.form['check_in'], '%d-%m-%Y %H:%M %p')
        education = datetime.strptime(request.form['depature'], '%d-%m-%Y %H:%M %p')
        housing_status = request.form["status"]

        update_customer_data = Customer.query.get(id)
        update_customer_data.age = age
        update_customer_data.job = job
        update_customer_data.marital_status = marital_status
        update_customer_data.education = education
        update_customer_data.housing_status = housing_status
        db.session.commit()

        return redirect("/show_all_customer", code=302)
    else:
        new_customer = Customer.query.get(id)
        new_customer.age = new_customer.age
        new_customer.job = new_customer.job

    return render_template('update_customer_data.html', title='Update Customer Data', customer=new_customer)


@customers.route("/customer_profile", methods=['POST', 'GET'])
@login_required
def customer_profile():
    #id = int(request.form["id"])
    present_customer = Customer.query.get(41344)
    #present_customer.age = present_customer.age  # type: object
    return render_template('customer_profile.html', title='Customer Profile', customer=present_customer)


@customers.route('/customer_results', methods=['POST', 'GET'])
@login_required
def customer_results():
    return redirect('/all_customer_results')


@customers.route('/customer_page', methods=['POST'])
@login_required
def customer_page():
    return redirect('/customer_page')

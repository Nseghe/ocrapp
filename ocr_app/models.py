from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from ocr_app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	posts = db.relationship('Post', backref='author', lazy=True)

	def get_reset_token(self, expires_sec=1800):
		s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
		return s.dumps({'user_id': self.id}).decode('utf-8')

	@staticmethod
	def verify_reset_token(token):
		s = Serializer(current_app.config['SECRET_KEY'])
		try:
			user_id = s.loads(token)['user_id']
		except:
			return None
		return User.query.get(user_id)

	def __repr__(self):
		return "User('{}', '{}', '{}')".format(self.username, self.email, self.image_file)


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return "Post('{}', '{}')".format(self.title, self.date_posted)


class Customer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	age = db.Column(db.Integer, nullable=False)
	job = db.Column(db.String(20), nullable=False)
	marital_status = db.Column(db.String(20), nullable=False)
	education = db.Column(db.String(20), nullable=False)
	credit_default = db.Column(db.String(10), nullable=False)
	account_balance = db.Column(db.Integer, nullable=False)
	housing_status = db.Column(db.String(20), nullable=False)
	existing_loan = db.Column(db.String(10), nullable=False)
	contact_mode = db.Column(db.String(20), nullable=False)
	days_since_last_contact = db.Column(db.Integer, nullable=False)
	month_of_last_contact = db.Column(db.String(20), nullable=False)
	duration_of_last_contact = db.Column(db.Integer, nullable=False)
	no_of_campaigns = db.Column(db.Integer, nullable=False)
	days_since_last_campaign = db.Column(db.Integer, nullable=False)
	no_of_contacts_during_campaign = db.Column(db.Integer, nullable=False)
	outcome_of_previous_campaign = db.Column(db.String(20), nullable=False)

	def __repr__(self):
		return "Customer('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(self.age,
				self.job, self.marital_status, self.education, self.credit_default,
				self.account_balance, self.housing_status, self.existing_loan)
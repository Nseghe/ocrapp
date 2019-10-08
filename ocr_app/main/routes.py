from flask import render_template, request, Blueprint

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')


@main.route("/testing/<string:temp>")
def testing(temp):
    temp = temp
    return render_template("tester.html", temp=temp)

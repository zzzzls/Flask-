from FlaskApp.views import home
from flask import render_template

@home.route("/")
def view():
    return render_template("home/index.html")

@home.route("/index")
def index():
    return "this is home's index"



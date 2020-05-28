from FlaskApp.views import login
from flask import render_template

@login.route("/")
def view():
    return render_template("login/index.html")

@login.route("/index")
def index():
    return "this is login's index"



from flask import Blueprint

home = Blueprint("home",__name__)
login = Blueprint("login",__name__)

from .home import home
from .login import login


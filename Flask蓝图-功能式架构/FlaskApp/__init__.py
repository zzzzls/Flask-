from flask import Flask
from FlaskApp.views import home
from FlaskApp.views import login

app = Flask(__name__)

app.register_blueprint(home,url_prefix="/home")
app.register_blueprint(login,url_prefix="/login")

print(home.root_path)
app.run()
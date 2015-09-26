# from flask.ext.login import LoginManager
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
manager = Manager(app)
mail = Mail(app)
# lm = LoginManager()
# lm.init_app(app)
# lm.login_view = 'login'

from app import views, models



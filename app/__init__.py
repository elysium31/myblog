# from flask.ext.login import LoginManager
from flask import Flask
from flask_script import Manager
# from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

flask_app = Flask(__name__)
flask_app.config.from_object('config')
manager = Manager(flask_app)
mail = Mail(flask_app)


from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(flask_app)


from app.services.database import db
db.app = flask_app
db.init_app(flask_app)

from app.blueprints import post_bp, site_bp, auth_bp
flask_app.register_blueprint(post_bp)
flask_app.register_blueprint(site_bp)
flask_app.register_blueprint(auth_bp)

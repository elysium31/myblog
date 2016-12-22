from flask import Flask
from flask_script import Manager
from flask_mail import Mail

flask_app = Flask(__name__)
flask_app.config.from_object('config')
manager = Manager(flask_app)
mail = Mail(flask_app)


from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(flask_app)

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()
bcrypt.init_app(flask_app)

from flask_wtf.csrf import CsrfProtect
csrf_protect = CsrfProtect()
csrf_protect.init_app(flask_app)

from app.services.database import db
db.app = flask_app
db.init_app(flask_app)


from app.blueprints import post_bp, site_bp, auth_bp
flask_app.register_blueprint(post_bp)
flask_app.register_blueprint(site_bp)
flask_app.register_blueprint(auth_bp)

from app.lib.url import url_current
flask_app.jinja_env.globals.update(
    url_current=url_current
)

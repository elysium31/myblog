from flask import Blueprint

post_bp = Blueprint('post', __name__)
# profile_bp = Blueprint('profile', __name__)
site_bp = Blueprint('site', __name__)
auth_bp = Blueprint('auth', __name__)

from .site import views
from .post import views
from .auth import views

from app.services.database import db
from flask_login import UserMixin
from sqlalchemy.types import Unicode, Integer, SmallInteger, DateTime
from sqlalchemy.ext.hybrid import hybrid_property
from flask_bcrypt import generate_password_hash, check_password_hash


ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model, UserMixin):
    id = db.Column(Integer, primary_key=True)
    username = db.Column(Unicode(64), index=True, unique=True)
    _password = db.Column("password", Unicode(255), nullable=False)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = generate_password_hash(plaintext)

    def is_correct_password(self, plaintext):
        return check_password_hash(self._password, plaintext)

    email = db.Column(Unicode(120), index=True, unique=True)
    date_confirmed = db.Column(DateTime())
    role = db.Column(SmallInteger, default=ROLE_USER)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    status = db.Column(db.SmallInteger(), nullable=False, server_default='0')

    __tablename__ = 'users'

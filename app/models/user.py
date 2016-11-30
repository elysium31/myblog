from app.services.database import db

ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    email = db.Column(db.String(120), index=True, unique=True)
    date_confirmed = db.Column(db.DateTime())
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    status = db.Column(db.SmallInteger(), nullable=False, server_default='0')

    __tablename__ = 'users'
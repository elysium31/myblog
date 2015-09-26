from app import app, db
from flask_user import UserMixin, SQLAlchemyAdapter, UserManager

ROLE_USER = 0
ROLE_ADMIN = 1


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    email = db.Column(db.String(120), index=True, unique=True)
    confirmed_at = db.Column(db.DateTime())
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    active = db.Column(db.Boolean(), nullable=False, server_default='0')

    # User information
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='0')

    def __repr__(self):
        return '<User %r>' % self.nickname


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    body = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Post %r>' % self.body

db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter, app)
DEBUG = True

PG_DB_KWARGS = dict(
   user_name="postgres",
   password="postgres",
   db_name="posts",
)
SQLALCHEMY_DATABASE_URI = (
   "postgresql://{user_name}:{password}@localhost:5432/{db_name}".format(**PG_DB_KWARGS)
)

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'


# Flask-Mail settings
MAIL_USERNAME = None
MAIL_PASSWORD = None
MAIL_SERVER = 'localhost'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TLS = False

ADMINS = [
    '"Admin One" <admin1@gmail.com>',
    ]
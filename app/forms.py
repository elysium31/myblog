from flask.ext.wtf import Form
from flask_user.forms import RegisterForm
from wtforms import StringField, BooleanField, SubmitField, validators
# from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[validators.DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class PostForm(Form):
    title = StringField('title', validators=[validators.DataRequired()])
    body = StringField('body', validators=[validators.DataRequired()])


class MyRegisterForm(RegisterForm):
    first_name = StringField('First name', validators=[
        validators.DataRequired('First name is required')])
    last_name = StringField('Last name', validators=[
        validators.DataRequired('Last name is required')])




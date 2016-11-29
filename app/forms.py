from flask_wtf import Form

from wtforms import StringField, BooleanField, SubmitField, validators
# from wtforms.validators import DataRequired


class LoginForm(Form):
    openid = StringField('openid', validators=[validators.DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class PostForm(Form):
    title = StringField('title', validators=[validators.DataRequired()])
    body = StringField('body', validators=[validators.DataRequired()])


class RegisterForm(Form):
    nickname = StringField(
        label='First name',
        validators=[
            validators.DataRequired('Nick name is required')
        ]
    )
    password = StringField(
        label='Last name',
        validators=[
            validators.DataRequired('Password is required')
        ]
    )




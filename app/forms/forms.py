from app.forms.form_base import FormBase

from wtforms import (
    StringField,
    BooleanField,
    SubmitField,
    PasswordField
)
from wtforms.validators import DataRequired


class LoginForm(FormBase):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class PostForm(FormBase):
    title = StringField('title', validators=[DataRequired()])
    body = StringField('body', validators=[DataRequired()])


class RegisterForm(FormBase):
    username = StringField(
        label='User name',
        validators=[
            DataRequired('User name is required')
        ]
    )
    password = PasswordField(
        label='Password',
        validators=[
            DataRequired('Password is required')
        ]
    )
    submit = SubmitField("Submit")



from app.forms.form_base import FormBase

from wtforms import (
    StringField,
    SubmitField,
    PasswordField
)
from wtforms.validators import DataRequired


class LoginForm(FormBase):
    email = StringField(
        label='Email',
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


class PostForm(FormBase):
    title = StringField(label='title', validators=[DataRequired()])
    body = StringField(label='body', validators=[DataRequired()])


class RegisterForm(FormBase):
    email = StringField(
        label='Email',
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

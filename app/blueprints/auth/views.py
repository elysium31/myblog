from flask import render_template, redirect, url_for, request
from flask_login import logout_user, login_user

from app.blueprints import auth_bp
from app.forms.forms import RegisterForm, LoginForm
from app.models.user import User
from app.services.database import db


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('site.index'))


@auth_bp.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm(formdata=request.form)
    if form.validate_on_submit():
        user = (
            User.query
            .filter(User.email == form.email.data)
            .first()
        )
        if user and user.is_correct_password(form.password.data):
            login_user(user)
            return redirect(url_for('site.index'))
        else:
            return redirect(url_for('auth.login'))
    return render_template('login.html', form=form)


@auth_bp.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm(formdata=request.form)
    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('site.index'))
    return render_template('register.html', form=form)


from flask import render_template, redirect, url_for, request
from flask_login import logout_user

from app.blueprints import auth_bp
from app.forms.forms import RegisterForm
from app.models.user import User
from app.services.database import db


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@auth_bp.route('/login')
def login():
    return render_template('login.html')


@auth_bp.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm(formdata=request.form)
    if request.method == 'POST':
        user = User()
        form.populate_obj(user)
        db.session.add(user)
        db.session.commit()
    return render_template('register.html', form=form)


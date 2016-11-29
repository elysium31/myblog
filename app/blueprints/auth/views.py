from flask import render_template, redirect, url_for
from flask_login import logout_user
from app.blueprints import auth_bp
from app.forms import RegisterForm


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@auth_bp.route('/login')
def login():
    return render_template('login.html')


@auth_bp.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)


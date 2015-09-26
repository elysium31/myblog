from flask import render_template, flash, redirect, url_for, g, request, session
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, models
# from oauth import OAuthSignIn
# from forms import PostForm, LoginForm
# from models import User, ROLE_USER, ROLE_ADMIN
import datetime

@app.route('/')
@app.route('/index')
def index():
    posts = models.Post.query.all()
    return render_template("index.html", posts=posts)


@app.route('/createpost', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        u = models.User.query.get(1)
        post_ = models.Post(title=title, body=body, timestamp=datetime.datetime.utcnow(), author=u)
        db.session.add(post_)
        db.session.commit()
        # flash('Your post is now live!')
        return redirect(url_for('index'))
    return render_template("new_post.html")


@app.route("/post/<int:post_id>")
def post(post_id):
    post = models.Post.query.get(post_id)
    return render_template("post.html", title=post.title, text=post.body)


# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('index'))
#
#
# @app.route('/login')
# def login():
#     return render_template('login.html')
#
#
# @app.before_request
# def before_request():
#     g.user = current_user


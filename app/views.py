from flask import render_template, flash, redirect, url_for, g, request, session
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, models, lm
from oauth import OAuthSignIn
from forms import PostForm, LoginForm
from models import User, ROLE_USER, ROLE_ADMIN
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


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/login')
def login():
    return render_template('login.html')


@app.before_request
def before_request():
    g.user = current_user


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous():
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()


@app.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous():
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    social_id, username, email = oauth.callback()
    if social_id is None:
        flash('Authentication failed.')
        return redirect(url_for('index'))
    user = User.query.filter_by(social_id=social_id).first()
    if not user:
        user = User(social_id=social_id, nickname=username, email=email)
        db.session.add(user)
        db.session.commit()
    login_user(user, True)
    return redirect(url_for('index'))
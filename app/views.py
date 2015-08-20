from flask import render_template, flash, redirect, url_for, g, request, session
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, models, lm, oid
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


@app.route("/login", methods=["GET", "POST"])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        session["remember_me"] = form.remember_me
    return render_template("login.html", title="Sign In", form=form, providers=app.config['OPENID_PROVIDERS'])


@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email, role=ROLE_USER)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember=remember_me)
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.before_request
def before_request():
    g.user = current_user
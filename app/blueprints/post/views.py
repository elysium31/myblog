import datetime

from flask import render_template, render_template_string, redirect, url_for, \
    request
from flask_login import login_required

from app.blueprints import post_bp
from app.models.user import User
from app.models.post import Post
from app.services.database import db


@post_bp.route('/createpost', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        u = User.query.get(1)
        post_ = Post(title=title, body=body, timestamp=datetime.datetime.utcnow(), author=u)
        db.session.add(post_)
        db.session.commit()
        # flash('Your post is now live!')
        return redirect(url_for('index'))
    return render_template("new_post.html")


@post_bp.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get(post_id)
    return render_template("post.html", title=post.title, text=post.body)


@post_bp.route("/test_post")
def test_post():
    return render_template_string('test post')



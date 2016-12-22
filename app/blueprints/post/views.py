import datetime

from flask import render_template, render_template_string, redirect, url_for, \
    request
from flask_login import login_required, current_user

from app.blueprints import post_bp
from app.forms.forms import NewPostForm
from app.models.post import Post
from app.services.database import db


@post_bp.route('/createpost', methods=['GET', 'POST'])
@login_required
def create_post():
    form = NewPostForm(formdata=request.form)
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            body=form.body.data,
            date_created=datetime.datetime.utcnow(),
            user_id=current_user.id
        )
        db.session.add(post)
        db.session.commit()
        # flash('Your post is now live!')
        return redirect(url_for('site.index'))
    return render_template("new_post.html", t_form=form)


@post_bp.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get(post_id)
    return render_template("post.html", title=post.title, text=post.body)

from flask import render_template, render_template_string

from app.blueprints import site_bp
from app.models.post import Post


@site_bp.route('/')
@site_bp.route('/index')
def index():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)

from flask import render_template
from app.blueprints import site_bp
from app.models.post import Post
from app.lib.pagination import Paginator


@site_bp.route('/')
@site_bp.route('/index')
@site_bp.route('/page<int:page>')
def index(page=1):
    paginator = Paginator(
        query=Post.query.order_by(Post.date_created.desc()),
        page=page,
        per_page=20)
    return render_template("index.html", t_paginator=paginator)

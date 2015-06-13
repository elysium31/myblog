from flask import render_template, redirect, url_for, g, request
from app import app, db, models
from forms import PostForm
import datetime

@app.route('/')
@app.route('/index')
def index():
    # posts = [
    #     {
    #         'id': 0,
    #         'title': "Title 1",
    #         'body': 'Beautiful day in Portland!'
    #     },
    #     {
    #         'id': 1,
    #         'title': "Title 2",
    #         'body': 'The Avengers movie was so cool!'
    #     },
    #     {
    #         'id': 2,
    #         'title': "Title 3",
    #         'body': "Something interesting"
    #     }
    #     ]
    posts = models.Post.query.all()
    return render_template("index.html", posts=posts)


@app.route('/createpost', methods=['GET', 'POST'])
def create_post():

    if request.method == 'POST':
        title = request.form.get('title')
        body = request.form.get('body')
        u = models.User.query.get(1)
        post_ = models.Post(title=title, body=body,
                            timestamp=datetime.datetime.utcnow(), author=u)
        db.session.add(post_)
        db.session.commit()
        # flash('Your post is now live!')
        return redirect(url_for('index'))
    return render_template("new_post.html")


@app.route("/post/<int:post_id>")
def post(post_id):
    post = models.Post.query.get(post_id)
    return render_template("post.html", title=post.title, text=post.body)

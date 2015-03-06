from flask import render_template, g
from app import app


@app.route('/')
@app.route('/index')
def index():
    posts = [
        {
            'id': 0,
            'title': "Title 1",
            'body': 'Beautiful day in Portland!'
        },
        {
            'id': 1,
            'title': "Title 2",
            'body': 'The Avengers movie was so cool!'
        }
        ]
    return render_template("index.html", posts=posts)

@app.route("/post/<int:post_id>")
def post(post_id):
    text = "This is post id: {}".format(post_id)
    return render_template("post.html", title=text, text=text)

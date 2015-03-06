from flask import render_template, g
from app import app


@app.route('/')
@app.route('/index')
def index():
    posts = [
        {
            'title': "Title 1",
            'body': 'Beautiful day in Portland!'
        },
        {
            'title': "Title 2",
            'body': 'The Avengers movie was so cool!'
        }
        ]
    return render_template("index.html", posts=posts)

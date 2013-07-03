"""View handler. """

from flask import render_template, abort

from twodaemon import app
from twodaemon.content import Content, ContentNotFoundError

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/articles/<article_name>")
def articles(article_name):
    content = Content("article", article_name)
    try:
        content.initialise()
        article = content.build_page()
    except ContentNotFoundError:
        abort(404)
    return render_template('article.html', **article)

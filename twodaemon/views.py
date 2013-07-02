"""View handler. """

from flask import render_template
from flask import Markup

from twodaemon import app
from twodaemon.articles import load_article

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/articles/<article_name>")
def articles(article_name):
    article_content = Markup(load_article(article_name))
    return render_template('article.html', title=article_name, content=article_content)

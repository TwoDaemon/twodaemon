"""View handler. """

from flask import render_template, abort

from twodaemon import app
from twodaemon.article import Article, ArticleNotFoundError

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/articles/<article_name>")
@app.route("/articles/<article_name>/<int:page_number>")
def articles(article_name, page_number=1):
    article = Article("article", article_name)
    try:
        article.initialise()
        page = article.build_page(page_number)
    except ArticleNotFoundError:
        abort(404)
    return render_template('article.html', **page)

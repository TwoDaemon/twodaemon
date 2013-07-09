"""View handler. """

from flask import render_template, abort

from twodaemon import app
from twodaemon.article import Article, ArticleNotFoundError, article_list

@app.route("/")
def home():
    return render_template('home.html', title="Home")

@app.route("/articles/")
def articles_list():
    articles = article_list("article")
    return render_template('articles_list.html', title="Articles", article_list=articles)

@app.route("/articles/<article_name>")
@app.route("/articles/<article_name>/<int:page_number>")
def article_single(article_name, page_number=1):
    article = Article("article", article_name)
    try:
        article.initialise()
        page = article.build_page(page_number)
    except ArticleNotFoundError:
        abort(404)
    return render_template('article.html', title=page['article_title'], **page)

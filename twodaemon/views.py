"""View handler. """

from flask import render_template, abort, redirect, url_for

from twodaemon import app, cache
from twodaemon import article

@app.route("/")
@cache.cached(timeout=app.config['CACHE_TIMEOUT'])
def home():
    return render_template('home.html', title="Home")

@app.route("/about")
@cache.cached(timeout=app.config['CACHE_TIMEOUT'])
def about():
    return render_template('about.html', title="About")

@app.route("/articles/")
@cache.cached(timeout=app.config['CACHE_TIMEOUT'])
def article_list():
    articles = article.list()
    return render_template('articles_list.html', title="Articles", article_list=articles)

@app.route("/articles/<article_name>")
@cache.cached(timeout=app.config['CACHE_TIMEOUT'])
def article_single(article_name):
    try:
        article_ = article.load(article_name)
    except article.ArticleNotFoundError:
        abort(404)
    return render_template('article.html', title=article_['title'], article=article_)

@app.route("/articles/<article_name>/<int:page_number>")
def article_paged_redirect(article_name, page_number):
    """We don't use page numbers anymore, so 301 redirect just in case. """
    return redirect(url_for('article_single', article_name=article_name), 301)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title="404 Not Found"), 404

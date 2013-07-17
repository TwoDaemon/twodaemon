"""View handler. """

from flask import render_template, abort

from twodaemon import app, cache
from twodaemon import article

@cache.cached(timeout=app.config['CACHE_TIMEOUT'])
@app.route("/")
def home():
    return render_template('home.html', title="Home")

@cache.cached(timeout=app.config['CACHE_TIMEOUT'])
@app.route("/about")
def about():
    return render_template('about.html', title="About")

@cache.cached(timeout=app.config['CACHE_TIMEOUT'])
@app.route("/blog")
def blog():
    return render_template('blog.html', title="Blog")

@cache.cached(timeout=app.config['CACHE_TIMEOUT'])
@app.route("/articles/")
def article_list():
    articles = article.article_list("article")
    return render_template('articles_list.html', title="Articles", article_list=articles)

@cache.cached(timeout=app.config['CACHE_TIMEOUT'])
@app.route("/articles/<article_name>")
@app.route("/articles/<article_name>/<int:page_number>")
def article_single(article_name, page_number=1):
    article_ = article.Article("article", article_name)
    try:
        article_.initialise()
        page = article_.build_page(page_number)
    except article.ArticleNotFoundError:
        abort(404)
    return render_template('article.html', title=page['page_title'], **page)

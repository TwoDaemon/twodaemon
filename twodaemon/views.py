"""View handler. """

from flask import render_template, abort

from twodaemon import app, cache
from twodaemon import article, blog

@app.route("/")
@cache.cached(timeout=app.config['CACHE_TIMEOUT'])
def home():
    return render_template('home.html', title="Home")

@app.route("/about")
@cache.cached(timeout=app.config['CACHE_TIMEOUT'])
def about():
    return render_template('about.html', title="About")

@app.route("/blog")
@cache.cached(timeout=app.config['CACHE_TIMEOUT'])
def blog_list():
    return render_template('blog.html', title="Blog")

@app.route("/blog/<post_name>")
@cache.cached(timeout=app.config['CACHE_TIMEOUT'])
def blog_single(post_name):
    try:
        post = blog.build_post(post_name)
    except blog.PostNotFoundError:
        abort(404)
    return render_template('blog_single.html', title=post['post_title'], **post)

@app.route("/articles/")
@cache.cached(timeout=app.config['CACHE_TIMEOUT'])
def article_list():
    articles = article.article_list("article")
    return render_template('articles_list.html', title="Articles", article_list=articles)

@app.route("/articles/<article_name>")
@app.route("/articles/<article_name>/<int:page_number>")
@cache.cached(timeout=app.config['CACHE_TIMEOUT'])
def article_single(article_name, page_number=1):
    article_ = article.Article("article", article_name)
    try:
        article_.initialise()
        page = article_.build_page(page_number)
    except article.ArticleNotFoundError:
        abort(404)
    return render_template('article.html', title=page['page_title'], **page)

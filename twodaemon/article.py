"""Flask article loading module.  """

from os import listdir
from cStringIO import StringIO

from flask import Markup, url_for
from markdown import Markdown

from twodaemon import app

article_directory = "%s/content/articles" % app.root_path

def list():
    """Collect data for all existing articles.  """
    articles = []
    for article_file in listdir(article_directory):
        article_name = article_file[:-3]
        article = load(article_name)
        if 'hidden' not in article:
            articles.append(article)
    return articles

def load(article_name):
    """Load an article for page display.  """
    content, md = _load_md("%s/%s.md" % (article_directory, article_name))
    return _create_article(content, md, article_name)

def _load_md(filepath):
    """Load a markdown file.  """
    md = Markdown(extensions = app.config['MARKDOWN_EXTENSIONS'])
    contentIO = StringIO()
    try:
        with open(filepath, 'r') as f:
            md.convertFile(input=f, output=contentIO)
    except IOError as ioe:
        raise ArticleNotFoundError("Article file '%s' not found." % filepath)
    content = contentIO.getvalue()
    contentIO.close()
    return content, md

def _create_article(content, md, name):
    """Create an article dict from required information.  """
    article = {key: meta[0] for key, meta in md.Meta.iteritems()}
    article.update({
        'name': name,
        'content': Markup(content),
        'url': url_for('article_single', article_name=name),
        'absolute_url': url_for('article_single', article_name=name, _external=True),
    })
    return article


class ArticleNotFoundError(Exception):
    """Exception thrown when the given article cannot be found.  """

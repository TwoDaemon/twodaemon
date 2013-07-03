"""Flask article loading module.  """

from markdown import markdown
from flask import Markup

from twodaemon import app

article_directory = "%s/content/articles" % app.root_path

def load_article(article_name):
    """Load an article from a markdown file.  """
    return markdown(_get_markdown_string_from_article_name(article_name))

def _get_markdown_string_from_article_name(article_name):
    """Load the markdown of an article as a string.  """
    try:
        with open("%s/%s.md" % (article_directory, article_name)) as f:
            markdown = f.read()
    except IOError as ioe:
        raise ArticleNotFoundError("Article file not found: %s/%s.md" % (article_directory, article_name))
    return markdown

class ArticleNotFoundError(Exception):
    """Exception thrown when an article cannot be found.  """

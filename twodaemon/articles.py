"""Flask article loading module.  """

# TODO: Shouldn't need this, see other todo.
import os

from markdown import markdown
from flask import Markup

# TODO: Update this later - should be in site config.
article_location = os.path.dirname(os.path.abspath(__file__))

def load_article(article_name):
    """Load an article from a markdown file.  """
    return markdown(_get_markdown_string_from_article_file(article_name))

def _get_markdown_string_from_article_file(article_name):
    """Load the markdown of an article as a string.  """
    with open("%s/%s.md" % (article_location, article_name)) as f:
        markdown = f.read()
    return markdown

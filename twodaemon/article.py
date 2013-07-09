"""Flask article loading module.  """

from os import listdir
from os.path import isdir

from flask import Markup
from flask import url_for
from markdown import markdown
import yaml

from twodaemon import app


def article_list(article_type):
    """Collect data for all existing articles.  """
    type_path = "%s/%s" % (Article.prefix_directory, article_type)
    articles = []
    for article_name in listdir(type_path):
        article = Article(article_type, article_name)
        article.initialise()
        articles.append(article.build_article_meta())
    return articles


class Article(object):
    """Load page content for multi-page articles."""

    prefix_directory = "%s/content" % app.root_path

    def __init__(self, article_type, article_name):
        self.type = article_type
        self.name = article_name
        self.config = None

    def initialise(self):
        self._check_article_directory()
        self._load_config()

    def build_article_meta(self):
        return {
            "article_name": self.name,
            "article_type": self.type,
            "article_url": url_for('article_single', article_name=self.name),
            "article_title": self.config['title'],
            "page_count": len(self.config['pages']),
        }

    def build_page(self, page_number):
        page_config = self._get_page_config(page_number)
        page = self.build_article_meta()
        page.update({
            "page_title": page_config['title'],
            "page_url": url_for('article_single', article_name=self.name, page_number=page_number),
            "page_number": page_number,
            "page_content": self._load_page_content(page_config),
        })
        return page

    def _check_article_directory(self):
        self.location = "%s/%s/%s" % (Article.prefix_directory, self.type, self.name)
        if not isdir(self.location):
            raise ArticleNotFoundError("Directory for article '%s' of type '%s' at %s not found." % (self.name, self.type, self.location))

    def _load_config(self):
        try:
            with open("%s/meta.yaml" % self.location, 'r') as f:
                self.config = yaml.load(f)
        except IOError:
            raise ArticleConfigNotFoundError("Config file for article '%s' of type %s' not found." % (self.name, self.type))
        except yaml.YAMLError as ye:
            raise ArticleConfigLoadError("Error reading config YAML: %s" % ye.message)

    def _get_page_config(self, page_number):
        try:
            return self.config['pages'][page_number]
        except KeyError as ke:
            raise ArticlePageNotFoundError("Definition for page %i not found in config for %s: %s" % (page_number, self.type, self.name))

    def _load_page_content(self, page_data):
        file_content = self._load_page_file_content(page_data['file'])
        return Markup(markdown(file_content))

    def _load_page_file_content(self, page_file):
        try:
            with open("%s/%s" % (self.location, page_file), 'r') as f:
                return f.read()
        except IOError as ioe:
            raise ArticlePageNotFoundError("Article file '%s' of type '%s' not found." % (page_file, self.type))


class ArticleLoadError(Exception):
    """Exception thrown when there are errors in loading the article.  """

class ArticleConfigLoadError(ArticleLoadError):
    """Exception thrown when there are errors loading an article config file.  """

class ArticleNotFoundError(Exception):
    """Exception thrown when the given article cannot be found.  """

class ArticleConfigNotFoundError(ArticleNotFoundError):
    """Exception thrown when an article config file cannot be found.  """

class ArticlePageNotFoundError(ArticleNotFoundError):
    """Exception thrown when an article page cannot be found.  """

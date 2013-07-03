"""Flask content loading module.  """

from os.path import isdir

from flask import Markup
from markdown import markdown
import yaml

from twodaemon import app

class Content(object):
    """Load page content for multi-page content items."""

    content_directory = "%s/content" % app.root_path

    def __init__(self, content_type, content_name):
        self.type = content_type
        self.name = content_name
        self.config = None

    def initialise(self):
        self._load_content_directory()
        self._load_config()

    def build_page(self):
        content = markdown(self._load_page_file_content())
        return self._build_page_dict(content)

    def _build_page_dict(self, content):
        return {
            "title": self.config['title'],
            "content": Markup(content),
        }

    def _load_content_directory(self):
        self.location = "%s/%s/%s" % (Content.content_directory, self.type, self.name)
        if not isdir(self.location):
            raise ContentNotFoundError("Directory for content '%s' of type '%s' at %s not found." % (self.name, self.type, self.location))

    def _load_config(self):
        try:
            with open("%s/%s.yaml" % (self.location, self.name), 'r') as f:
                self.config = yaml.load(f)
        except IOError:
            raise ContentConfigNotFoundError("Config file for content '%s' of type %s' not found." % (self.name, self.type))
        except yaml.YAMLError as ye:
            raise ContentConfigLoadError("Error reading config YAML: %s" % ye.message)

    def _load_page_file_content(self):
        try:
            with open("%s/%s" % (self.location, self.config['content_file']), 'r') as f:
                return f.read()
        except IOError as ioe:
            raise ContentPageNotFoundError("Content file '%s' of type %s' not found." % (self.config['content_file'], self.type))


class ContentLoadError(Exception):
    """Exception thrown when there are errors in loading the content item.  """

class ContentConfigLoadError(ContentLoadError):
    """Exception thrown when there are errors loading a content config file.  """

class ContentNotFoundError(Exception):
    """Exception thrown when the given content cannot be found.  """

class ContentConfigNotFoundError(ContentNotFoundError):
    """Exception thrown when a content config file cannot be found.  """

class ContentPageNotFoundError(ContentNotFoundError):
    """Exception thrown when a content page cannot be found.  """

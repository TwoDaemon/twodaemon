"""Flask content loading module.  """

from markdown import markdown

from twodaemon import app

content_directory = "%s/content" % app.root_path

def load_content(content_type, content_name):
    """Load page content from a markdown file.  """
    return markdown(_get_markdown_string_by_content(content_type, content_name))

def _get_markdown_string_by_content(content_type, content_name):
    """Load the markdown of a content item as a string.  """
    try:
        with open(_get_content_file_location(content_type, content_name)) as f:
            markdown = f.read()
    except IOError as ioe:
        raise ContentNotFoundError("Content file '%s' of type %s' not found." % (content_type, content_name))
    return markdown

def _get_content_file_location(content_type, content_name):
    return "%s/%s/%s.md" % (content_directory, content_type, content_name)

class ContentNotFoundError(Exception):
    """Exception thrown when a content item cannot be found.  """

"""Flask blog loading module.  """

from os import listdir
from os.path import isdir

from flask import Markup
from flask import url_for
from markdown import Markdown

from twodaemon import app

prefix_directory = "%s/content" % app.root_path

def build_post(post_name):
    file_content = _load_post_file_content(post_name)
    md = Markdown(extensions = ['meta'])
    content = _modify_content(md.convert(file_content))
    meta = _build_meta(md.Meta, post_name)
    meta['post_content'] = content
    return meta

def _load_post_file_content(post_name):
    try:
        with open("%s/blog/%s.md" % (prefix_directory, post_name), 'r') as f:
            return f.read()
    except IOError as ioe:
        raise PostNotFoundError("Post file '%s.md' not found." % (post_name))

def _modify_content(content):
    return Markup(content)

def _build_meta(meta, post_name):
    return {
        'post_name': post_name,
        'post_title': meta['title'][0],
        'url': url_for('blog_single', post_name=post_name),
        'absolute_url': url_for('blog_single', post_name=post_name, _external=True),
    }


class PostNotFoundError(Exception):
    """Error when the post file cannot be found."""

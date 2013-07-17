from flask import Flask
from flask.ext.cache import Cache

app = Flask('twodaemon')

app.config.from_object('twodaemon.settings')

# Disable caching in debug mode.
if app.debug:
    app.config['CACHE_TYPE'] = 'null';
cache = Cache(app)

import twodaemon.views

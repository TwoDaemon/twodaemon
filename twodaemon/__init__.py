from flask import Flask
from flask.ext.cache import Cache

app = Flask('twodaemon')

app.config.from_object('twodaemon.settings')

cache = Cache(app)
#cache = Cache(app, config={'CACHE_TYPE': 'null'})

import twodaemon.views

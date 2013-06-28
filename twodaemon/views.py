"""View handler. """

from twodaemon import app

@app.route("/")
def hello():
    return "Hello World!"

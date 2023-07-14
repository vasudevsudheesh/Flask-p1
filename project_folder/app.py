from flask import Flask

test = Flask(__name__)


@test.route("/profile/<username>")
def home(username):
    return "<h1>  this is the profile of %s <h1>" % username

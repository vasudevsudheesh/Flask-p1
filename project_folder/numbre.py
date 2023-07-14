from flask import Flask

test = Flask(__name__)


@test.route("/profile/<int:id>")
def home(id):
    return "<h1>  this is the profile of %d <h1>" % id

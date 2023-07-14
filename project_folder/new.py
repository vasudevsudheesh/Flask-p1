from flask import Flask
new=Flask(__name__)


@new.route('/')
def home():
    return '<h1>  hello new world <h1>'


@new.route(('/new'))
def new1():
    return '<h1>new next page </h1>'
new.run()
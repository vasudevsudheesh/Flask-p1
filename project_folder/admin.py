from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/profile/<username>")
def profile(username):
    return render_template("profile.html", username=username, isactive=True)


@app.route("/books")
def book():
    book_names = [
        "Django for Beginners",
        "Django Web Development Cookbook",
        "Two Scoops of Django",
        "Django Design Patterns and Best Practices",
        "Test-Driven Development with Python",
        "Django Unleashed",
        "Django RESTful Web Services",
        "Practical Django Projects",
        "Learning Django Web Development",
        "Django By Example",
    ]

    return render_template("book.html", books=book_names)


app.run(debug=True)

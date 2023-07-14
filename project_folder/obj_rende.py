from flask import Flask, render_template

app = Flask(__name__)


@app.route("/books_rende")
def book():
    book_authors = [
        {
            "book": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "cover": "https://blog-cdn.reedsy.com/directories/admin/featured_image/591/medium_dissecting-the-cover-of-a-book-ee0d6a.jpg",
        },
        {
            "book": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "cover": "https://blog-cdn.reedsy.com/directories/admin/featured_image/591/medium_dissecting-the-cover-of-a-book-ee0d6a.jpg",
        },
        {
            "book": "1984",
            "author": "George Orwell",
            "cover": "https://blog-cdn.reedsy.com/directories/admin/featured_image/591/medium_dissecting-the-cover-of-a-book-ee0d6a.jpg",
        },
        {
            "book": "Pride and Prejudice",
            "author": "Jane Austen",
            "cover": "https://blog-cdn.reedsy.com/directories/admin/featured_image/591/medium_dissecting-the-cover-of-a-book-ee0d6a.jpg",
        },
        {
            "book": "The Catcher in the Rye",
            "author": "J.D. Salinger",
            "cover": "https://blog-cdn.reedsy.com/directories/admin/featured_image/591/medium_dissecting-the-cover-of-a-book-ee0d6a.jpg",
        },
        {
            "book": "Moby Dick",
            "author": "Herman Melville",
            "cover": "https://blog-cdn.reedsy.com/directories/admin/featured_image/591/medium_dissecting-the-cover-of-a-book-ee0d6a.jpg",
        },
        {
            "book": "The Lord of the Rings",
            "author": "J.R.R. Tolkien",
            "cover": "https://blog-cdn.reedsy.com/directories/admin/featured_image/591/medium_dissecting-the-cover-of-a-book-ee0d6a.jpg",
        },
        {
            "book": "The Chronicles of Narnia",
            "author": "C.S. Lewis",
            "cover": "https://blog-cdn.reedsy.com/directories/admin/featured_image/591/medium_dissecting-the-cover-of-a-book-ee0d6a.jpg",
        },
        {
            "book": "Harry Potter and the Philosopher's Stone",
            "author": "J.K. Rowling",
            "cover": "https://blog-cdn.reedsy.com/directories/admin/featured_image/591/medium_dissecting-the-cover-of-a-book-ee0d6a.jpg",
        },
        {
            "book": "The Hunger Games",
            "author": "Suzanne Collins",
            "cover": "https://blog-cdn.reedsy.com/directories/admin/featured_image/591/medium_dissecting-the-cover-of-a-book-ee0d6a.jpg",
        },
        {
            "book": "aaaa",
            "author": "sss",
            "cover": "https://blog-cdn.reedsy.com/directories/admin/featured_image/591/medium_dissecting-the-cover-of-a-book-ee0d6a.jpg",
        },
    ]

    return render_template("book_rende.html", books=book_authors)


app.run(debug=True)

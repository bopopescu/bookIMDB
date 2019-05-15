# -----------------------------------------
# main.py
# creating first flask application
# -----------------------------------------
#

from flask import Flask, render_template, request
from create_db import app, db, Book, create_books, Author, Publisher, create_publishers, create_authors
from sqlalchemy import desc, asc, func
from partial_resources import books_head, authors_head, publishers_head




@app.route('/')
def splash():
    return render_template('splash.html')


@app.route('/books/')
def books():
    books = db.session.query(Book).all()
    return render_template('books.html', books_data=books, books_head=books_head)


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/authors/')
def authors():
    authors = db.session.query(Author).all()
    books = db.session.query(Book).all()


    return render_template('authors.html', authors_data=authors, authors_head=authors_head)


@app.route('/publishers/')
def publishers():
    publishers = db.session.query(Publisher).all()
    return render_template('publishers.html', publishers_data=publishers, publishers_head=publishers_head)


@app.route('/books/<id>')
def book(id):
    books = db.session.query(Book).all()
    for book in books:
        if book.id == int(id):
            data = book
            break

    return render_template("book.html", book=data)


@app.route('/authors/<id>')
def author(id):
    books = db.session.query(Book).filter_by(authorID=id).all()
    authors = db.session.query(Author).all()
    for author in authors:
        if author.id == int(id):
            data = author
            break

    return render_template("author.html", author=data, books_data=books)


@app.route('/publishers/<id>')
def publisher(id):
    books = db.session.query(Book).filter_by(pubID=id).all()
    publishers = db.session.query(Publisher).all()
    for publisher in publishers:
        if publisher.id == int(id):
            data = publisher
            break

    return render_template("publisher.html", publisher=data, books_data=books)

@app.route('/search/', methods=['POST'])
def search():
    user_search = request.form['user_search']
    search_in = str(user_search).lower()

    books = db.session.query(Book).filter(func.lower(
        Book.title).like("%" + search_in + "%")).from_self()
    authors = db.session.query(Author).filter(func.lower(
        Author.name).like("%" + search_in + "%")).from_self()
    publishers = db.session.query(Publisher).filter(func.lower(
        Publisher.name).like("%" + search_in + "%")).from_self()

    
    # books = db.session.query(Book).filter_by(pubID=id).all()
    return render_template('search.html', books_data=books, authors_data=authors, publishers_data=publishers,books_head=books_head, authors_head=authors_head, publishers_head=publishers_head)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)

# ---------------------host ='134.2-------------------
# end of main.py
# -----------------------------------------

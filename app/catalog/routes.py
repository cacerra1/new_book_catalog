from app.catalog import main
from app import db
from app.catalog.models import Book, Publication
from flask import render_template, flash, request, redirect, url_for
from flask_login import login_required
from app.catalog.forms import EditBookForm, CreateBookForm # we import these from oue catalog/forms.py


@main.route('/')
def display_books():
    books = Book.query.all()
    return render_template('home.html', books=books)


@main.route('/display/publisher/<publisher_id>')
def display_publisher(publisher_id):
    publisher = Publication.query.filter_by(id=publisher_id).first()
    publisher_books = Book.query.filter_by(pub_id=publisher.id).all()
    return render_template('publisher.html',
                           publisher=publisher,
                           publisher_books=publisher_books)


@main.route('/book/delete/<book_id>', methods=['GET', 'POST'])
@login_required #means users need to be logged in to delete books
def delete_book(book_id):
    book = Book.query.get(book_id)  #query book id from DB
    if request.method == 'POST':
        db.session.delete(book)
        db.session.commit()
        flash('book delete successfully')
        return redirect(url_for('main.display_books'))
    return render_template('delete_book.html', book=book, book_id=book.id) # if not post request go to the delete page


@main.route('/edit/book/<book_id>', methods=['GET', 'POST']) # book_id is a variable that represents the book we want to delete
@login_required  #means users need to be logged in to delete books
def edit_book(book_id):
    book = Book.query.get(book_id) # query database for the book we need to update
    form = EditBookForm(obj=book)
    if form.validate_on_submit():
        book.title = form.title.data # value is gotten from form
        book.format = form.format.data
        book.num_pages = form.num_pages.data
        db.session.add(book) # add it and commit it to the DB
        db.session.commit()
        flash('Book Edited Successfully')
        return redirect(url_for('main.display_books'))
    return render_template('edit_book.html', form=form) # get displays the form


@main.route('/create/book/<pub_id>', methods=['GET', 'POST'])
@login_required
def create_book(pub_id):
    form = CreateBookForm() # this imports the form to create the book
    form.pub_id.data = pub_id  # pre-populates pub_id
    if form.validate_on_submit(): # if post request
        book = Book(title=form.title.data, author=form.author.data, avg_rating=form.avg_rating.data,
                    book_format=form.format.data, image=form.img_url.data, num_pages=form.num_pages.data,
                    pub_id=form.pub_id.data)
        db.session.add(book)
        db.session.commit()
        flash('Book added successfully')
        return redirect(url_for('main.display_publisher', publisher_id=pub_id))
    return render_template('create_book.html', form=form, pub_id=pub_id) # get displays the form

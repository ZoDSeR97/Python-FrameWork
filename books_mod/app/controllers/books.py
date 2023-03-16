from app import app
from app.models import book, user
from flask import render_template, request, redirect, session

@app.route('/books')
def books():
    return render_template('books.html', books=book.Book.get_all())

@app.route('/books/<int:id>')
def booksInfo(id):
    return render_template('book.html', book=book.Book.get_one({'id':id}), users=user.User.get_all_notFav({'id':id}))

@app.route('/newBook', methods=['POST'])
def newBook():
    book.Book.save(request.form)
    return redirect('/books')

@app.route('/newFavUser', methods=['POST'])
def newFavUser():
    info = request.form['info'].split()
    data = {
        'books_id': int(info[0]),
        'users_id': int(info[1]),
    }
    user.User.save_fav(data)
    return redirect('/books/'+info[0])
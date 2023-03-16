from app import app
from flask import render_template, request, redirect, session
from app.models import user, book

@app.route('/')
def home():
    return redirect('/authors')

@app.route('/authors')
def index():
    return render_template('index.html', authors=user.User.get_all())

@app.route('/authors/<int:id>')
def authorInfo(id):
    return render_template('author.html', author=user.User.get_one({'id':id}), books=book.Book.get_all_notFav({'id':id}))

@app.route('/newAuthor', methods=['POST'])
def newAuthor():
    user.User.save(request.form)
    return redirect('/')

@app.route('/newFavBook', methods=['POST'])
def newFavBook():
    info = request.form['info'].split()
    data = {
        'books_id': int(info[0]),
        'users_id': int(info[1]),
    }
    user.User.save_fav(data)
    return redirect('/authors/'+info[1])

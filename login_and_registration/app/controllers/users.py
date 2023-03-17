from app import app, bcrypt
from app.models import user
from flask import render_template, redirect, request, session
import secrets

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect('/')
    return render_template("profile.html", user=user.User.get_one({'id':session['user_id']})[0])

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    # see if the login information provided valid
    if not user.User.validate_login(request.form):
        return redirect('/')
    user_in_db = user.User.get_one(request.form, condition='email')
    session['user_id'] = user_in_db[0].id
    # never render on a post!!!
    return redirect("/profile")

@app.route('/register', methods=['POST'])
def register():
    if user.User.validate_registration(request.form):
        salt = secrets.token_hex()
        pw_hash = bcrypt.generate_password_hash(request.form['password']+salt)
        print(pw_hash, len(pw_hash))
        # put the pw_hash into the data dictionary
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': pw_hash,
            'mumbo_jumbo': salt
        }
        # Call the save @classmethod on User
        user_id = user.User.save(data)
        # store user id into session
        session['user_id'] = user_id
    return redirect('/')

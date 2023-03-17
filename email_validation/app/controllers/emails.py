from app import app
from app.models import email
from flask import render_template, request, redirect, session

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/dashboard')
def home():
    return render_template("history.html", emails=email.Email.get_all(), newEmail=email.Email.get_last())


@app.route('/register', methods=['POST'])
def register():
    if not email.Email.is_valid(request.form):
        # we redirect to the template with the form.
        return redirect('/')
    # ... do other things
    email.Email.save(request.form)
    return redirect('/dashboard')
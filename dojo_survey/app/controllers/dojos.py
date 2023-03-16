from app import app
from app.models import dojo
from flask import render_template, request, redirect, session

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result')
def result():
    return render_template("receipt.html", dojo=dojo.Dojo.get_last())

@app.route('/submit', methods=['POST'])
def collect():
    if dojo.Dojo.is_valid(request.form):
        dojo.Dojo.save(request.form)
        return redirect('/result')
    else:
        print("___INVALID FORM___")
        return redirect('/')
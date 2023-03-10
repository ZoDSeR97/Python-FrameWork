import secrets
from random import randint
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = secrets.token_hex()

@app.route('/')
def index():
    gotIt = False
    hint = ""
    color = "bg-danger"
    if 'num' not in session:
        session['num'] = randint(1, 100)
    if "guess" not in session:
        session['guess'] = 0
    if "res" not in session:
        session['res'] = False
    if "att" not in session:
        session['att'] = 1
    elif session['att'] < 5:
        if int(session['guess']) < session['num']:
            hint = "Too Low!"
        elif int(session['guess']) > session['num']: 
            hint = "Too High!"
        else:
            hint = str(session['num'])+" was the number, took "+str(session['att'])+" attempts"
            color = "bg-success"
            gotIt = True
        session['att']+=1
    else:
        gotIt = True
        hint = "You Lose!"
    return render_template("index.html", gotIt=gotIt, hint=hint, color=color)


@app.route('/process', methods=['POST'])
def process():
    session['guess'] = request.form['guessNum']
    session['res'] = True
    return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

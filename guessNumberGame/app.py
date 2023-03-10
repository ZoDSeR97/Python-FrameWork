import secrets
from random import randint
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = secrets.token_hex()

@app.route('/')
def index():
    # Initialize secret number
    if 'num' not in session:
        session['num'] = randint(1, 100)
    
    # Initialize attempts
    if "att" not in session:
        session['att'] = 1
    
    # Initialize Game State
    if "gameOver" not in session:
        session["gameOver"] = False
    
    return render_template("index.html")


@app.route('/process', methods=['POST'])
def process():
    if request.form['guessNum'].isdigit():
        session['guess'] = int(request.form['guessNum'])
        session['att']+=1
        session['gameOver'] = session['guess']==session['num'] or session['att'] == 6
    return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

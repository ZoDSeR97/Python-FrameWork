import secrets
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = secrets.token_hex()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/result')
def result():
    return render_template("result.html", name=session['name'], location=session['location'], lang=session['favLang'], comment=session['comment'])


@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['favLang'] = request.form['lang']
    session['comment'] = request.form['comment']
    return redirect('/result')


if __name__ == "__main__":
    app.run(debug=True)

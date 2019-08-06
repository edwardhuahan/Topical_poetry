import os
from flask import Flask, flash, request, redirect, url_for, render_template
import run

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/', methods=['GET', 'POST'])
@app.route('/index/')
def upload_file():
    if request.method == 'POST':
        word = request.form['word']
        if word:
            print(word)
            return run.generate(word)
        
    return render_template('index.html', poem="")

if __name__ == "__main__":
    app.run()
from logging import debug
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 5050)

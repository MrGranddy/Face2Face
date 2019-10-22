from flask import Flask
from flask import render_template, request, redirect, url_for, session

app = Flask(__name__)


@app.route('/login')
def login():
    if request.method == "GET":
        return render_template("pages/temp.html")

@app.route('/')
def home():
    if request.method == "GET":
        return render_template("pages/temp.html")

@app.route('/register')
def register():
    if request.method == "GET":
        return render_template("pages/temp.html")

@app.route('/compare')
def compare():
    if request.method == "GET":
        return render_template("pages/temp.html")

if __name__ == '__main__':
    app.run()
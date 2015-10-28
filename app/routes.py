from flask import Flask, render_template
from flask.ext.script import Manager
from .forms import NameForm
from app import app


@app.route('/')
def home():
    form = NameForm()
    print "hello"
    return render_template(
        'home.html',
        form=form)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

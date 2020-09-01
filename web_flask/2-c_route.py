#!/usr/bin/python3
''' script that starts a Flask web application '''

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    ''' Route Hello HBNB! '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbtn():
    ''' Route display HBNB '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    ''' Route C is <text> '''
    return 'C {}'.format(text.replace('_', ' '))

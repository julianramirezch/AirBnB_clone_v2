#!/usr/bin/python3
''' script that starts a Flask web application '''

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    ''' Function return Hello HBNB! '''
    return 'Hello HBNB!'

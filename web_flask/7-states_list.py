#!/usr/bin/python3
'''  script that starts a Flask web application '''

from flask import Flask, render_template
from models import storage, State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    ''' remove the current SQLAlchemy Session'''
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    ''' Display HTML page States '''
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
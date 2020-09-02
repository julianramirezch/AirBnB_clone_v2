#!/usr/bin/python3
'''  script that starts a Flask web application '''

from flask import Flask, render_template
from models import storage, State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    ''' Display HTML page States '''
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    ''' Display HTML page States by id '''
    state = None
    states = storage.all(State)
    key = 'State.{}'.format(id)
    if key in states:
        state = states[key]
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown_db(error):
    ''' remove the current SQLAlchemy Session'''
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

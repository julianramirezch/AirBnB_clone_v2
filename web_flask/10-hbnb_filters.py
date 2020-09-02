#!/usr/bin/python3
''' script that starts a Flask web application '''

from flask import Flask, render_template
from models import storage, State, Amenity

app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    ''' Show HBNB clone States, cities and amenity'''
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_db(error):
    ''' remove the current SQLAlchemy Session'''
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

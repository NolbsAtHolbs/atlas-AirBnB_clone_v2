#!/usr/bin/python3
"""Module for starting a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all(State).values()
    states_ordered = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=states_ordered)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

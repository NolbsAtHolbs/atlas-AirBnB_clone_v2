#!/usr/bin/python3
"""Module for starting a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display HTML of states and cities"""
    states_all = storage.all(State)
    states = {state_id: state for state_id, state in states_all.items()}
    states_ordered = sorted(states.values(), key=lambda x: x.name)
    for state in states_ordered:
        state.cities.sort(key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states_ordered)


@app.teardown_appcontext
def teardown(exception):
    """Closes SQLAlchemy"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

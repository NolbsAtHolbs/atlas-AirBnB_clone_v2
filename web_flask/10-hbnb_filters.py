#!/usr/bin/python3
"""Module for starting a Flask web application"""

import sys
from flask import Flask
from flask import render_template
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    storage.close()

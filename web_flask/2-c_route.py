#!/usr/bin/python3
'''Module for starting a Flask web application'''

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

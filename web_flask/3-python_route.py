#!/usr/bin/python3
"""
This script starts a Flask web application.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Returns a greeting message for the home page.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns a specific message for the HBNB page.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """
    Display “C ” followed by the value of the text variable.
    Replaces underscores in the text with spaces.
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """
    Display “Python ” followed by the value of the text variable.
    Replaces underscores in the text with spaces.
    """
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    # Run the application on host 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""
This script starts a simple Flask web application with multiple routes and template rendering.
"""

from flask import Flask, render_template
app = Flask(__name__)

# Define the route for the home page
@app.route('/', strict_slashes=False)
def index():
    """
    Returns a greeting message for the home page.
    """
    return 'Hello HBNB!'

# Define the route for /hbnb
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns a specific message for the HBNB page.
    """
    return 'HBNB'

# Define the route for /c/<text>
@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """
    Displays 'C ' followed by the value of the text variable.
    Underscores in the text variable are replaced with spaces.
    """
    modified_text = text.replace('_', ' ')
    return f'C {modified_text}'

# Define the route for /python and /python/<text>
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """
    Displays 'Python ' followed by the value of the text variable.
    Default value is 'is cool'. Underscores in the text variable are replaced with spaces.
    """
    modified_text = text.replace('_', ' ')
    return f'Python {modified_text}'

# Define the route for /number/<int:n>
@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """
    Displays 'n is a number' only if n is an integer.
    """
    return f"{n} is a number"

# Define the route for /number_template/<int:n>
@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """
    Displays an HTML page only if n is an integer.
    The HTML page is rendered using a template.
    """
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    # Run the application on host 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)

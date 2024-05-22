#!/usr/bin/python3
"""
This script starts a simple Flask web application that displays a list of states and their cities.
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Displays an HTML page with the states and their cities listed in alphabetical order.
    """
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the storage on teardown.
    This function is called after each request to ensure the database connection is properly closed.
    """
    storage.close()

if __name__ == '__main__':
    # Run the application on host 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)

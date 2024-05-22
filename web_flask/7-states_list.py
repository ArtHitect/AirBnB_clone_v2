#!/usr/bin/python3
"""
This script starts a simple Flask web application that displays a list of states.
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Displays an HTML page with the states listed in alphabetical order.
    """
    # Retrieve all State objects from storage and sort them by name
    states = sorted(list(storage.all("State").values()), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)

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

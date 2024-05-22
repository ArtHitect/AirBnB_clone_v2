#!/usr/bin/python3
"""
This script starts a simple Flask web application that displays states and their cities.
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """
    Displays an HTML page with the states and optionally, cities listed in alphabetical order.
    If a state_id is provided, it displays the cities of that state.
    """
    states = storage.all("State")
    selected_state = None
    if state_id:
        state_key = 'State.' + state_id
        selected_state = states.get(state_key)
    return render_template('9-states.html', states=states, selected_state=selected_state)

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

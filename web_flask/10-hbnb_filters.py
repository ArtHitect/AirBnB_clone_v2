#!/usr/bin/python3
"""
This script starts a Flask web application that displays HBNB filters.
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """
    Displays an HTML page similar to 6-index.html from the static folder.
    """
    # Retrieve all states and amenities from storage
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    
    # Render the template with the retrieved data
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)

@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the storage connection on teardown.
    """
    storage.close()

if __name__ == '__main__':
    # Run the application on host 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)

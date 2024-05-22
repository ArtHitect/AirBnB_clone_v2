#!/usr/bin/python3
"""
This script starts a simple Flask web application.
"""

from flask import Flask
app = Flask(__name__)

# Define the route for the home page
@app.route('/', strict_slashes=False)
def index():
    """
    Returns a greeting message for the home page.
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    # Run the application on host 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)

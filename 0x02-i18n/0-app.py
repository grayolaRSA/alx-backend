#!/usr/bin/env python3
"""module to setup a basic Flask app"""


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home() -> str:
    """function for simple app route with an html template"""
    return render_template('templates/0-index.html')


if __name__ == "__main__":
    """initialise app"""
    app.run()

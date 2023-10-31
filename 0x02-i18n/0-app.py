#!/usr/bin/env python3
"""module for Flask app"""


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home() -> str:
    """simple app home endpoint"""
    return "Hello World"


if __name__ == "__main__":
    """initialise app"""
    app.run()

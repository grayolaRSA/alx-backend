#!/usr/bin/env python3
"""module for Flask app"""


from flask import Flask, render_template
from flask_babel import Babel, _


app = Flask(__name__)


@app.route('/')
def home():
    """simple app home endpoint"""
    return render_template('templates/index.html')


if __name__ == '__main__':
    app.run()

#!/usr/bin/env python3
"""module for Flask app"""


from flask import Flask, render_template, request
from flask_babel import Babel, _


app = Flask(__name__)

babel = Babel(app)


class Config:
    """configuration class"""
    
    LANGUAGES = ["en", "fr"]

    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def home() -> str:
    """function for simple app route with an html template"""
    return render_template('templates/1-index.html')


if __name__ == '__main__':
    """initiate app"""
    app.run()

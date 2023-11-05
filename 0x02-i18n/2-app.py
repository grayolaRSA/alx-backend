#!/usr/bin/env python3
"""
module to setup a basic Flask app
"""


from flask import Flask, render_template, request
from flask_babel import Babel, _


app = Flask(__name__)

babel = Babel(app)


class Config:
    """
    configuration class for Babel setup
    """

    LANGUAGES: list = ["en", "fr"]

    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Select and return best language match based on supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def home() -> str:
    """
    Handles / route
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    """initiate app"""
    app.run(port="5000", host="0.0.0.0", debug=True)

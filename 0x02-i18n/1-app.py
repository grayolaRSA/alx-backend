#!/usr/bin/env python3
"""module for Flask app"""


from flask import Flask, render_template, request
from flask_babel import Babel, _


app = Flask(__name__)

babel = Babel(app)


class Config:
    """configuration class"""
    def __init__(self) -> None:
        """initialise configuration of app"""

        self.LANGUAGES = ["en", "fr"]

        user_language = request.accept_languages.best_match(app.config
                                                            ['LANGUAGES'])

        self.BABEL_DEFAULT_LOCALE = user_language
        self.BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def home():
    """simple app home endpoint"""
    return render_template('templates/1-index.html')


if __name__ == '__main__':
    app.run()

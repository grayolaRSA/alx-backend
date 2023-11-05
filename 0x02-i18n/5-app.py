#!/usr/bin/env python3
"""
module to setup a basic Flask app
"""
from flask import (
    Flask,
    render_template,
    request,
    g
)
from flask_babel import Babel
from typing import Dict, Union

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """
    configuration class for Babel setup
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    function to get users preferred language
    """
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    function for simple app route with an html template
    """
    return render_template('5-index.html')

def get_user():
    """
    function to get user that is logged in
    """
    user_id = request.args.get('login_as', None)
    if user_id is not None and int(user_id) in users.keys():
        return users.get(int(user_id))
    else:
        return None

@app.before_request
def before_request():
    """
    find a user and set it as the global user on Flask
    """
    user = get_user()
    g.user = user



if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)

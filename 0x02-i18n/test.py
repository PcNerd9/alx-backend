#!/usr/bin/env python3

"""
Flask wit flask_babel
"""
from flask import Flask, g,  render_template, request
from flask_babel import Babel
from typing import Dict, Union


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict[str, Union[str, None], None]]:
    """
    get the logged in user
    """
    user_id = request.args.get("login_as", None)
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    the configuration class for the flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """
    used to set the locale to use
    """
    locale = request.args.get("locale", None)
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.before_request
def before_request() -> None:
    """
    set the current user to the flask global var
    """
    user = get_user()
    if user:
        g.user = user
    else:
        g.user = None


@app.route("/", methods=["GET"])
def home() -> str:
    """
    the home route
    """
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run()

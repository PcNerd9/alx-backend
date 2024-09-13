#!/usr/bin/env python3

"""
Flask wit flask_babel
"""
from flask import Flask, g,  render_template, request
from flask_babel import Babel
import pytz
from typing import Dict


app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """
    used to get the locale to use
    """
    locale = request.args.get("locale", None)
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    elif g.user:
        locale = g.user.get("locale", None)
        if locale and locale in app.config["LANGUAGES"]:
            return locale
    elif request.headers.get("Accept-Language", None):
        return request.accept_languages.best_match(app.config["LANGUAGES"])
    else:
        return babel.default_locale


@babel.timezoneselector
def get_timezone() -> str:
    """
    used to the get the timezone to use
    """
    default_timezone = "UTC"
    timezone = request.args.get("timezone", None)
    if timezone:
        try:
            pytz.timezone(timezone)
        except pytz.exceptions.UnknownTimeZoneError:
            return default_timezone
        else:
            return timezone

    if g.user:
        timezone = g.user.get("timezone", None)
        try:
            pytz.timezone(timezone)
        except pytz.exceptions.UnknownTimeZoneError:
            return default_timezone
        else:
            return timezone
    return default_timezone


def get_user() -> Union[Dict[str, Union[str, None]], None]:
    """
    get the value of the current user
    """
    user_id = request.args.get("login_as", None)
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request() -> None:
    """
    set the value of the flask global variable
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
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run()

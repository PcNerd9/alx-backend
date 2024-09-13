#!/usr/bin/env python3

"""
Flask wit flask_babel
"""
from flask import Flask, g,  render_template, request
from flask_babel import Babel
from typing import Dict, Union


app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    the configuration class to use for the flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """
    use to set the value of  the locale to use
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


def get_user() -> Union[Dict[str, Union[str, None]], None]:
    """
    get the current logged in user
    """
    user_id = request.args.get("login_as", None)
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request() -> None:
    """
    use to set the value of the flask global var
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
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run()

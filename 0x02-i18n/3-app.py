#!/usr/bin/env python3

"""
Flask wit flask_babel
"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    a configuration class for the flask app
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
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", methods=["GET"])
def home() -> str:
    """"
    the home route"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run()

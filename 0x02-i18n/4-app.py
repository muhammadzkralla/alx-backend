#!/usr/bin/env python3

"""
4. Hello world Flask app with template and langs.
"""

import re
import babel
from flask import Flask, render_template, request
from flask_babel import Babel


class Config():
    """ Configuration for babel translation """
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config.from_object(Config())
Babel.default_locale = "en"
Babel.default_timezone = "UTC"
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ get_locale function implementation. """
    lang = request.args.get('locale')
    if lang is not None:
        if lang in app.config['LANGUAGES']:
            return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ Return Hello World template with langs. """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
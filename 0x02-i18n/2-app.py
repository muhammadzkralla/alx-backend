#!/usr/bin/env python3

"""
2. Hello world Flask app with template and langs.
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ get_locale function implementation. """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ Return Hello World template with langs. """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

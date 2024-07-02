#!/usr/bin/env python3
"""Basic Flask application"""

from flask import Flask, render_template, request
from flask_babel import Babel
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Get local"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def home() -> str:
    """Home route"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

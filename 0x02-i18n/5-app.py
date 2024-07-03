#!/usr/bin/env python3
"""Basic Flask application"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from config import Config


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config.from_object(Config)
app.jinja_env.add_extension('jinja2.ext.i18n')
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Get local"""
    print(request.args)
    local = request.args.get('locale')
    if local and local in app.config['LANGUAGES']:
        return local
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> dict:
    """Get user"""
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request() -> None:
    """Before request"""
    user = get_user()
    g.user = user


@app.route('/', methods=['GET'], strict_slashes=False)
def home() -> str:
    """Home route"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")

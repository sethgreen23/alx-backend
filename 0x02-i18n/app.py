#!/usr/bin/env python3
"""Basic Flask application"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from config import Config
import pytz
from datetime import datetime


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
    local = request.args.get('locale')
    if local and local in app.config['LANGUAGES']:
        return local
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """Get timezone"""
    timezone = request.args.get('timezone')
    if timezone:
        try:
            timezone_check = pytz.timezone(timezone)
        except pytz.UnknownTimeZoneError:
            return app.config['BABEL_DEFAULT_TIMEZONE']
        return timezone
    if g.user and g.user['timezone']:
        try:
            timezone_check = pytz.timezone(g.user['timezone'])
        except pytz.UnknownTimeZoneError:
            return app.config['BABEL_DEFAULT_TIMEZONE']
        return g.user['timezone']
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.before_request
def before_request() -> None:
    """Before request"""
    user = get_user()
    if user:
        g.user = user
    else:
        g.user = None


def get_user() -> dict:
    """Get user"""
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.route('/', methods=['GET'], strict_slashes=False)
def home() -> str:
    """Home route"""
    user_timezone = get_timezone()
    utc_time = datetime.now(pytz.utc)
    local_time = utc_time.astimezone(pytz.timezone(user_timezone))
    formated_time = local_time.strftime("%b %d, %Y, %I:%M:%S %p")
    return render_template('6-index.html', currentTime=formated_time)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")

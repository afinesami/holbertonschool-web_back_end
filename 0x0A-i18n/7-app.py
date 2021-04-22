#!/usr/bin/env python3
''' Flask app '''

from flask import Flask, request, render_template, g
from flask_babel import Babel, gettext
import pytz

app = Flask(__name__)
babel = Babel(app)


class Config:
    ''' App config '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def before_request():
    ''' def before request '''
    g.user = get_user()


@babel.localeselector
def get_locale():
    ''' return best languages '''
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=["GET"], strict_slashes=False)
def hello_world():
    ''' return the template '''
    return render_template('5-index.html')


def get_user():
    ''' return the right dictionary '''
    Id = request.args.get('login_as')
    if Id and int(Id) in users:
        return users[int(Id)]
    else:
        return None

@babel.timezoneselector
def get_timezone():
    ''' the best time zone '''
    user_timez = request.args.get('timezone', None)
    if not user_timez and g.user:
        user_timez = g.user.get('timezone')
    if user_timez:
        try:
            return pytz.timezone(user_timez)
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return pytz.timezone(app.config['BABEL_DEFAULT_TIMEZONE'])


if __name__ == '__main__':
    app.run()

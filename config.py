import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class FlaskConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'verysupersecretkeystring'
    SESSION_TYPE = 'filesystem'

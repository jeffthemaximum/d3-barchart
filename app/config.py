import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://uaaalnaflmsjnp:pLyQ5JRVbro0WCgXuMVorfqSjY@ec2-54-227-255-240.compute-1.amazonaws.com:5432/d8hosmtv1eijgp'

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/owl5'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:jB3ahfHUTD0GVW4_@192.168.0.214/owl2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'test': DevelopmentConfig,
    'prod': ProductConfig,
}

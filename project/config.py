import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_PATH = os.path.join(os.getcwd(), "../project.db")


class BaseConfig:
    JSON_AS_ASCII = False

    ITEMS_PER_PAGE = 12

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    # SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_PATH}'
    SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:db_password@db/db_name'

import os
from dotenv import load_dotenv
import datetime
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    PROPAGATE_EXCEPTIONS = True
    SQLAlCHEMY_TRACK_MODIFICATIONS=False
    PROPAGATE_EXCEPTIONS=True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProductionConfig(Config):
    DEBUG = False
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=1)

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

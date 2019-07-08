import os

class Config:
    '''
    General configuration parent class
    '''
    # Creating the app configurations
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://tony:tonyqtjds2@localhost/myblog'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
    Config: THe parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://tony:tonyqtjds2@localhost/myblog'

class DevConfig(Config):
    '''
    Development configuration child class
    Args:
    Config: THe parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://tony:tonyqtjds2@localhost/myblog'
    DEBUG = True
    ENV = 'development'
config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}
    
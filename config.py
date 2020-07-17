import os

class Config:

    SECRET_KEY ='4167'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Mozzy123@localhost/pitch'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

class ProdConfig(Config):
    '''
    Parental production  configuration child class
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    '''
     The development  configuration child class
    '''
    
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://postgres:Mozzy123@localhost/pitch'
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}
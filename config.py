import os

class Config:

    SECRET_KEY ='4167'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Mozzy123@localhost/watchlist'

class ProdConfig(Config):
    '''
    Parental production  configuration child class
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    '''
     The development  configuration child class
    '''
    
    SQLALCHEMY_DATABASE_URI=''
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}
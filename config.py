import os

class Config:

    SECRET_KEY ='4167'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Mozzy123@localhost/watchlist'

class ProdConfig(Config):
    '''
    Parental production  configuration child class
    '''
    pass


class DevConfig(Config):
    '''
     The development  configuration child class
    '''

    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}
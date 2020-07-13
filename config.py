import os

class Config:

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY ='4167'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Mozzy123@localhost/watchlist'
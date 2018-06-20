
import os
class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = '1026e1f40ffff2d1e81963ed15818e53'
    SECRET_KEY = os.environ.get('12345')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://gabrielcoder:12345@localhost/watchlist'




class ProdConfig(Config):
    '''
    Pruduction  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}   
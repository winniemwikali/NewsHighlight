import os
class Config:

    NEWS_API_SOURCES_URL = 'https://newsapi.org/v2/sources?language=&country={}&apiKey={}'
    ARTICLE_API_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    
   

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
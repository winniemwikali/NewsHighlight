import os
class Config:

    NEWS_API_SOURCES_URL = 'https://newsapi.org/v2/sources?language=en&country={}&category={}&apiKey={}'
    ARTICLE_API_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'news'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY') or 'cbc8be6a9903427d9ebda4efa81fc3a3' 
    
   

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
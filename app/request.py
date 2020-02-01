import urllib.request,json
from .models import Articles
from .models import Source

# Getting api key
api_key = None
# Getting the movie base url
base_url = None
#
source_url =None

def configure_request(app):
    global api_key,base_url,source_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['ARTICLE_API_SOURSES_URL']
    source_url = app.config['ARTICLE_API_BASE_URL']

def get_news (country,category):
    '''
    function of getting json response 
    '''
    get_news_url = base_url.format(country,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_result = None


        if get_news_response['sources']:
            news_result_list = get_news_response['sources']
            news_result = process_results(news_result_list)

    return news_result


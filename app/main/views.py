from flask import render_template
from . import main
from ..request import get_news,get_details

#Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    
    general_list = get_news('us','general')
    business_list = get_news('us','business')
    technology_list = get_news('us','technology')
    sports_list = get_news('us','sports')
    health_list = get_news('us','health')
    science_list = get_news('us','science')
    entertainment_list = get_news('us','entertainment')
    return render_template('index.html',general=general_list,business=business_list,technology=technology_list,sports=sports_list,health=health_list,science=science_list,entertainment=entertainment_list)
@main.route('/news')
def news():
    """
    View articles that returns news article from a highlight
    """
    news_args = get_details(id)
    highlight_args = 'Route Working' 
    # name = k'{results_list}
    return render_template('news.html',highlight_param=highlight_args,news=news_args)   
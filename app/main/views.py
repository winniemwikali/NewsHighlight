from flask import render_template
from . import main
from ..request import get_news,get_updates

#Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    political_list = get_news('kenya','political')
    business_list = get_news('kenya','business')
    sports_list = get_news ('kenya','sports')
    economy_list = get_news('kenya','economy')
    technology_list = get_news('kenya','technology')
    return render_template('index.html',political=political_list,business=business_list,sports=sports_list,economy=economy_list,technology=technology_list)
@main.route('/news<id>')
def news(id):
    """
    View articles that returns news article from a highlight
    """
    news_args = get_updates(id)
    highlight_args = 'Route Working' 
    # name = k'{results_list}'
    return render_template('news.html',highlight_param=highlight_args,news=news_args)   
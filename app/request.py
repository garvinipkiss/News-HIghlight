# from app import app
import urllib.request
import json
from .models import Source
from .models import Articles

# Source = news_source.Source
# Articles = news_articles.Articles

# Getting the api_key
api_key = None
# Getting the base_url
base_url = None
# Getting source url
source_url = None


def configure_request(app):
    global api_key, base_url, source_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['BASE_NEWS_API_URL']
    source_url = app.config['SOURCE_NEWS_URL']


def get_sources(coutry, category):
    """
    Function that gets the json response to our url request
    """
    get_news_url = base_url.format(coutry, category, api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        # print(get_news_response)
        # get_news_response is now a dictionary because of the json.loads()

        source_results = None

        if get_news_response['sources']:
            source_results_list = get_news_response['sources']
            source_results = process_sources(source_results_list)

    return source_results


def process_sources(source_list):
    """
    We now want to process the dictionary and
    output a list of objects - news_results.
    We process results will transform our dictionary into a list of objects.
    """

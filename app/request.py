import urllib.request,json
from .models import Source, Articles

#api key
api_key = None

#base urls
news_source_url = None
article_url = None

def configure_request(app):
  global api_key,news_source_url,article_url
  api_key = app.config['NEWS_API_KEY']
  news_source_url = app.config['NEWS_SOURCE_API_BASE_URL']
  article_url = app.config['NEWS_ARTICLE_BASE_URL']

def get_source(category):
  """
  """
  get_source_url = news_source_url.format(category)

  with urllib.request.urlopen(get_source_url) as url:
    get_source_data = url.read()
    get_source_response = json.loads(get_source_data)

    source_results = None

    if get_source_response['sources']:
      source_result_list =get_source_response['sources']

      source_results = process_results(source_result_list)

  return source_results

def process_results(source_list):
  """
  """
  source_results = []

  for source_item in source_list:
    id = source_item.get('id')
    name = source_item.get('name')
    description = source_item.get('description')
    url = source_item.get('url')
    category = source_item.get('category')

    source_object = Source(id,name,description,url,category)
    source_results.append(source_object)

  return source_results

def get_article(source):
  get_article_url = article_url.format(source,api_key)
  # get_article_url = 'https://newsapi.org/v1/articles?source=the-new-york-times&apiKey=e2ddbdf56d69495489a40f4d451bb2b8'

  with urllib.request.urlopen(get_article_url) as url:
    get_article_data = url.read()
    get_article_data_response = json.loads(get_article_data)

    article_results = None

    if get_article_data_response['articles']:
      article_results_list = get_article_data_response['articles']
      article_results = process_article_results(article_results_list)
      # print(article_results)
  # print(article_results)
  return article_results

def process_article_results(article_results):
  """
  """

  article_list = []

  for article_item in article_results:
    author = article_item.get('author')
    title = article_item.get('title')
    description = article_item.get('description')
    url = article_item.get('url')
    picture = article_item.get('urlToImage')
    date= article_item.get('publishedAt')

    # if date:
    article_object = Articles(author,title,description,url,picture,date)
    print(article_object)
    article_list.append(article_object)

  print(article_list)
  return article_list

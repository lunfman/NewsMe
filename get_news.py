try:
    import requests
except ModuleNotFoundError:
    # for vscode
    import pip._vendor.requests as requests

import datetime
TODAY = datetime.datetime.today().date()
# API Ref
"""
qInTitle - Keywords or phrases to search for in the article title only.
q - Keywords or phrases to search for in the article title and body.

sortBy
The order to sort the articles in. Possible options: relevancy, popularity, publishedAt.
relevancy = articles more closely related to q come first.
popularity = articles from popular sources and publishers come first.
publishedAt = newest articles come first.
"""

class GetNews:
    def __init__(self, api_key, url='https://newsapi.org/v2/everything'):
        self.API_KEY = api_key
        self.API_URL = url
        # stores found news after running get news method
        # news data stores in the next format -> {key_word:[{}]} if used get=list
        # without method next format -> [{key_word:extracted_news_string}]
        self.found_news = []

    """
    def get_news returns the string of news by default
    * also possible return list by adding parameter get = 'list'
    """
    """
    One main argument key_word accepts string of interested topic
    Optionals:
    - language en, rus or etc possible
    - date = from witch date by default today
    - article_number how many articles we want to get by default 5
    - search_type - check api ref above
    - sort - check api ref above
    """

    def get_news(self, key_word, language='en', date=TODAY, articles_number=5,
                 search_type="qInTitle", sort='popularity', **kwargs):

        parameters = {
            search_type: key_word,
            'from': date,
            'sortBy': sort,
            'language': language,
            'apiKey': self.API_KEY,
        }

        response = requests.get(self.API_URL, params=parameters)
        data = response.json()
        if data['status'] != 'ok':
            raise Exception ('Your API Key invalid')

        # Checking for any news. If we received 0 news or data < articles number we are going to say that article number
        # = to results this will allow to escape key or index errors in the future
        if data['totalResults'] == 0 or data['totalResults'] < articles_number:
            articles_number = data['totalResults']
            print(f'Results for {key_word.strip()}:{articles_number}')

        # checking for optional params
        for key, value in kwargs.items():
            if key == 'get':
                if value == 'list':
                    # if user want to get list after exe
                    news_articles = []
                    for number in range(articles_number):
                        articles = data['articles'][number]
                        news_articles.append(articles)
                    news_list = [key_word, news_articles]
                    return self.found_news.append(news_list)
        # if user did not used optional params function return string of news
        # instances for return
        news = ''

        # looping through api data and extracting news
        for number in range(articles_number):
            articles = data['articles'][number]
            article_source = articles['source']['name']
            article_title = articles['title']
            article_content = articles['content']
            article_url = articles['url']
            news += f"{article_source}\n{article_title}\n{article_content}\n{article_url}\n\n"
        # saveing to found_news as string
        return self.found_news.append({key_word:news})

try:
    import requests
except ModuleNotFoundError:
    # for vscode
    import pip._vendor.requests as requests

import datetime
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

    def __init__(self, api_key):
        # api key and endpoints
        self.API_KEY = api_key
        self.everything_endpoint = 'https://newsapi.org/v2/everything'
        self.top_headlines_endpoint = 'https://newsapi.org/v2/top-headlines'

        # dates
        self.today = datetime.datetime.today().date()   
        # date = today
        self.date = self.today

        # default parameters
        self.def_params = {
            'qInTitle': '',
            'from': self.date,
            'sortBy': 'popularity',
            'language': 'en',
            'apiKey': self.API_KEY,
        }
        # number of articles by deafault

        self.articles_num = 5
        # stores api response in json format
        self.api_data = ''

    """
    One main argument key_word accepts string of interested topic
    Optionals:
    - language en, rus or etc possible
    - date = from witch date by default today
    - article_number how many articles we want to get by default 5
    - search_type - check api ref above
    - sort - check api ref above
    """


    def create_params(self, **kwargs):
        # overwrite existing parameters
        self.def_params = {}
        for key, value in kwargs.items():
            pass
        pass
   

    def get_everything(self, keyword):
        self.def_params['qInTitle'] = keyword

        response = requests.get(self.everything_endpoint, params=self.def_params)
        self.api_data = response.json()
        
        if self.api_data['status'] != 'ok':
            raise Exception ('Your API Key invalid')
        # if all good extract articles array from api data for forward use
        self.articles = self.api_data['articles'][:self.articles_num]
        
        return self

    def get_list(self):
        # return a list with articles from articles
        return [article for article in self.articles]


    def show_news(self):
        # this method just prints the news in formated way
        news = ''
        # looping through api data and extracting news
        # articles = api_data[articles]and slice this list by articles num
        
        for article in self.articles:
            article_source = article['source']['name']
            article_title = article['title']
            article_content = article['content']
            article_url = article['url']
            news += f"{article_source}\n{article_title}\n{article_content}\n{article_url}\n\n"
        
        print(news)
        return self

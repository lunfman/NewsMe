import unittest
#from unittest.mock import Mock
import json
from get_news import GetNews
import os

path = f'{os.path.dirname(os.path.realpath(__file__))}/data.json'
with open(path) as json_file:
    data = json.load(json_file)

class TestGetNewsClass(unittest.TestCase):
    
    def setUp(self):
        self.news = GetNews('api key')
        self.news.api_data = data
        

    def test_get_list(self):
        self.news.articles_num = 2
        self.news.articles = self.news.api_data['articles'][:self.news.articles_num]
        self.assertLessEqual(len(self.news.get_list()), 2)

        self.assertEqual(len(self.news.get_list()), 2)

        self.news.articles_num = 1
        self.news.articles = self.news.api_data['articles'][:self.news.articles_num]
        self.assertLessEqual(len(self.news.get_list()), 1)

        self.assertEqual(len(self.news.get_list()), 1)

    def test_new_params(self):
        self.assertEqual(self.news.new_params(language='a', date = 'b').params,
            {'language':'a', 'date':'b', 'apiKey': 'api key'})

    def test_search(self):
        pass

if __name__ == '__main__':
    unittest.main()
# NewsApp
NewsApp allows users to create a list of interesting topics and get emails with the latest news in readable format.
Features:
* you can create own template by using html creator module
* you can interact with api by changing get_news functions parameters

## How to use?
* To use this app you need an api key from newsApi. 
* You need an email address to send emails.
* To receive email with interested topics you need to provide information in topics.txt
```
Topic1
Topic2
Topic3
ETC.
```

## Instalation
git clone repo
## Modules
### GetNews class
provide simple interaction with NewsApi by using get_news method
default end pont is 'https://newsapi.org/v2/everything'
```
from get_news import GetNews
news = GetNews(api_key='API_KEY', url='Endpoint')
```
#### get_news method
This method can interact with NewsApi   
Main argument key_word. -> What are you looking for?
Optional arguments : language='en', date=TODAY, articles_number=5, search_type="qInTitle", sort='popularity'
```
        parameters = {
            search_type: key_word,
            'from': date,
            'sortBy': sort,
            'language': language,
            'apiKey': self.API_KEY,
        }
```

from datetime import date
from html_creator import CreateHtml
from get_news import GetNews
#from mail import ShareNews
import os
# relative path to dir
path = os.path.dirname(os.path.realpath(__file__))
# List of topics for news search from topics.txt
file_path = f"{path}/topics.txt"
with open(file=file_path) as file:
    topics = [topic.strip() for topic in file.readlines()]

# Creating news class to get news from api
# api_key is needed (NewsApi)
news = GetNews(api_key='')

# running for loop to get topic from topics list and run news class to get latest news and append to the message
for topic in topics:
    news.get_news(topic, articles_number=2 ,date='2021-11-01', get='list')
# creating create html class
creator = CreateHtml()
# html_content is going to store converted strings returned as a list each
# html_content = []
# plain text will contain plain text for mail sending in case mail client do not support html messages
plain_text = ''
# html content string is going to store plain html text from html content
# html_content_string = ''

# running a for loop to get data from news.found_news
found_news = news.found_news
for number in range(len(found_news)):
    header = found_news[number][0]
    #html_header.append(creator.create_simple_html(h1=header))
    # checking if message list of dict longer than 0 if not pass
    if len(found_news[number][1]) > 0:
        # if message longer than 0 going to add values to the html_content
        # using create_simple_html with h1 = header to create header list after creation
        creator.create_simple_html(h1=header)
        # adding header to plain text
        plain_text += f'{header}\n'
        # current list = message[number][1] -> selecting list of articles
        cur_list = found_news[number][1]

        for article in cur_list:
            #print(article['title'])
            # getting values from dict ['title] and etc is from api usage  ----> check api
            title = article['title']
            text = article['content']
            url = article['url']
            # creating html
            creator.create_simple_html(b=title, p=text, a=url)
            # add to plain text
            plain_text += f'{title}\n{text}\n{url}\n'

# creating html, opening template, replaceing the content
creator.create_html().use_template().replace_templates_content()

# sending news
# init ShareNews class
#send = ShareNews(mail_to= os.environ['MY_MAIL'])
# opening template
#template = send.open_mail_template()
# sending html mail
#send.send_html_mail(template, html_content_string, plain_text)

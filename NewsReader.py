from html_creator import CreateHtml
from get_news import GetNews
from mail import ShareNews
import os
# relative path to dir
# path = os.path.dirname(os.path.realpath(__file__))
# # List of topics for news search from topics.txt
# file_path = f"{path}/topics.txt"
# with open(file=file_path) as file:ex
#     topics = [topic.strip() for topic in file.readlines()]

# Creating news class to get news from api
# api_key is needed (NewsApi)
#news = GetNews(api_key='')
#news.create_params(lang = 'test')
#news.show_news()
#news.get_everything('apple').show_news()

# running for loop to get topic from topics list and run news class to get latest news
# i am using get list to work with api data directly after exe
# if to use get_news without get it will return string with extracted news
# for topic in topics:
#     news.get_news(topic, get='list')

# creating create html class
# creator = CreateHtml()
# # stores plain text if mail do not support html....
# plain_text = ''

# running a for loop to extract data from news.found_news
# news.found_news stores all news which was collected duiring get_news method
# found_news = news.found_news
# for number in range(len(found_news)):
#     # header is the first element ['header', [articles]]
#     header = found_news[number][0]
#     # checking if message list of dict longer than 0 if not pass
#     if len(found_news[number][1]) > 0:
#         # if message longer than 0 going to add values to the html_content
#         # using create_simple_html with h1 = header to create header
#         creator.create_simple_html(h1=header)
#         # adding header to plain text
#         plain_text += f'{header}\n'
#         # current list = message[number][1] -> selecting list of articles
#         cur_list = found_news[number][1]

#         for article in cur_list:
#             # getting values from dict ['title] and etc is from api usage  ----> check api
#             title = article['title']
#             text = article['content']
#             url = article['url']
#             # creating single html block
#             creator.create_simple_html(b=title, p=text, a=url)
#             # add to plain text
#             plain_text += f'{title}\n{text}\n{url}\n'

# creating html, opening template, replaceing the content
#creator.create_html().use_template().replace_templates_content()

# sending news
# init ShareNews class
# provide the next information: mail, mail_to, mail - password, smtp_server, port - default 465, subject
# send = ShareNews(mail= 'sender mail', password= 'senders pass', mail_to= 'receiver',
#  smtp_server='providers smtp server', subject='subject name')
# sending html mail
#send.send_html_mail(creator.template, plain_text)

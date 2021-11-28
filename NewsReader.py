from html_creator import CreateHtml
from get_news import GetNews
from mail import ShareNews
import os

path = os.path.dirname(os.path.realpath(__file__))
# List of Interested topics for news search from topics.txt
file_path = f"{path}/topics.txt"
with open(file=file_path) as file:
    topics = [topic.strip() for topic in file.readlines()]

# Creating news class to get news from api
news = GetNews()
message = []

# running for loop to get topic from topics list and run news class to get latest news and append to the message
for topic in topics:
    message.append(news.get_news(topic, get='list'))
# creating create html class
creator = CreateHtml()
# instances for future work html_content going to store converted strings returned as a list each
html_content = []
# plain text will contain plain text for mail sending in case mail client do not support
plain_text = ''
# html content string is going to content plain html text from html content
html_content_string = ''

# running a for loop to get data from message
for number in range(len(message)):
    header = message[number][0]
    #html_header.append(creator.create_simple_html(h1=header))
    # checking if message list of dict longer than 0 if not pass
    if len(message[number][1]) > 0:
        # if message longer than 0 going to add values to the html_content
        # using create_simple_html with h1 = header to create header list after creation
        html_content.append(creator.create_simple_html(h1=header))
        # adding header to plain text
        plain_text += f'{header}\n'
        # current list = message[number][1] -> selecting list of articles
        cur_list = message[number][1]

        for article in cur_list:
            #print(article['title'])
            # getting values from dict ['title] and etc is from api usage  ----> check api
            title = article['title']
            text = article['content']
            url = article['url']
            html_content.append(creator.create_simple_html(b=title, p=text, a=url))
            plain_text += f'{title}\n{text}\n{url}\n'

# creating html content string
# create_simple_html returns list
for line in html_content:
    for value in line:
        print(value)
        html_content_string += f'{value}\n'

# sending news
# init ShareNews class
send = ShareNews(mail_to= os.environ['MY_MAIL'])
# opening template
template = send.open_mail_template()
# sending html mail
send.send_html_mail(template, html_content_string, plain_text)

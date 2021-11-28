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

# running for loop to get topic from topic list and run news class and append to the list
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

# running a for loop to get all list from message
# PLEASE RENAME X
for x in range(len(message)):
    header = message[x][0]
    #html_header.append(creator.create_simple_html(h1=header))
    # checking if message list of dict longer than 0 if not pass
    if len(message[x][1]) > 0:
        #print(header)
        # if message longer than 0 going to add values to the html_content list
        # using create_simple_html with h1 = header to create header this will return a list
        html_content.append(creator.create_simple_html(h1=header))
        # adding header to plain text
        plain_text += f'{header}\n'
        # current list = message[x][1] can be added before if statement
        cur_list = message[x][1]

        for x in cur_list:
            #print(x['title'])
            # getting values from dict ['title] and etc is from api usage  ----> check api
            title = x['title']
            text = x['content']
            url = x['url']
            html_content.append(creator.create_simple_html(b=title, p=text, a=url))
            plain_text += f'{title}\n{text}\n{url}\n'

# creating html content string
for line in html_content:
    for value in line:
        #print(value)
        html_content_string += f'{value}\n'

print(html_content_string)
# sending news
send = ShareNews(mail_to= os.environ['MY_MAIL'])
template = send.open_mail_template()

send.send_html_mail(template, html_content_string, plain_text)

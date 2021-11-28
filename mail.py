import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


class ShareNews:
    """
    ShareNews class by default need the next instances:
        -mail = senders_mail
        -mail_to = who will receive the mail
        -password = mails password
        -smtp_server = The server of you mail provider
        -port = Default 465

    Mail Instances:
        self.message = MIMEMultipart("alternative")
        self.message["Subject"] = "multipart test"
        self.message["From"] = self.MY_MAIL
        self.message["To"] = self.TO_MAIL


    def open_mail_template(path='template.html') -- > method to open html file by path by default = 'template.html'

    def send_html_mail(self, html_template, html_content, message_text):

    -html_template has to have [CONTENT] string for changeable part or replaceable perfectly in body
    -html_content - a string of html content
    -message text - plain text for sending without html tags
    """
    def __init__(self, mail= os.environ['MAIL'], mail_to= os.environ['MAIL'], password= os.environ['PASSWORD'],
                 smtp_server='smtp.yandex.ru', port='465'):
        # Connection Instances
        self.MY_MAIL = mail
        self.TO_MAIL = mail_to
        self.MAIL_PASSWORD = password
        self.SMTP_SERVER = smtp_server
        self.PORT = port

        # Mail / Message Instances
        self.message = MIMEMultipart("alternative")
        self.message["Subject"] = "multipart test"
        self.message["From"] = self.MY_MAIL
        self.message["To"] = self.TO_MAIL
    # put insdie of the function
    template_path = os.path.dirname(os.path.realpath(__file__))

    @staticmethod
    def open_mail_template(path=f'{template_path}/template.html'):
        with open(path) as html_template:
            html = html_template.read()
        return html

    def send_html_mail(self, html_template, html_content, message_text):
        message_html = html_template
        message_html = message_html.replace('[CONTENT]', html_content)

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(message_text, "plain")
        part2 = MIMEText(message_html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        self.message.attach(part1)
        self.message.attach(part2)

        with smtplib.SMTP_SSL(self.SMTP_SERVER, self.PORT) as server:
            server.login(self.MY_MAIL, self.MAIL_PASSWORD)
            server.sendmail(self.MY_MAIL, self.TO_MAIL, self.message.as_string())
            print('sent')

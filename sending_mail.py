from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

import const


def send_mail(message):
    with open('/Users/elizavetaantonova/Desktop/inst/питон/4 сем/ping/password.txt', 'r', encoding="UTF-8") as f:
        password = f.read().strip()

    msg = MIMEMultipart()
    msg['From'] = 'resultping@ya.ru'
    msg['To'] = const.mail
    msg['Subject'] = 'Result of tcping'

    msg.attach(MIMEText(message, 'plain'))
    with smtplib.SMTP('smtp.ya.ru: 587') as server:
        server.starttls()

        server.login(msg['From'], password)

        server.sendmail(msg['From'], msg['To'], msg.as_string())

    return f'Successfully sent email to {msg["To"]}'

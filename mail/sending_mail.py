from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from constants import const


def send_mail(message):
    with open(const.password_path, 'r', encoding="UTF-8") as f:
        password = f.read().strip()

    msg = MIMEMultipart()
    msg['From'] = 'resultping@ya.ru'
    msg['To'] = const.mail
    msg['Subject'] = 'Result of tcping'

    msg.attach(MIMEText(message, 'plain'))

    try:
        with smtplib.SMTP('smtp.ya.ru: 587') as server:
            server.starttls()
            server.login(msg['From'], password)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
        return f'Successfully sent email to {const.mail}'
    except smtplib.SMTPServerDisconnected:
        return f'The server {const.mail} is not responding'
    except smtplib.SMTPException:
        return f'Something gone wrong'

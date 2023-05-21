import smtplib

import pytest

from constants import const
from mail.sending_mail import send_mail


class TestSendingMail:
    def test_send_mail(self):
        const.mail = 'la-work-hard@yandex.ru'
        assert send_mail('test') is True
        with pytest.raises(smtplib.SMTPServerDisconnected):
            raise smtplib.SMTPServerDisconnected
        with pytest.raises(smtplib.SMTPException):
            raise smtplib.SMTPException

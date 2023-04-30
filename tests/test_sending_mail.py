import const
from sending_mail import send_mail


class TestSendingMail:
    def test_send_mail(self):
        const.mail = 'la-work-hard@yandex.ru'
        assert send_mail('test') == 'Successfully sent email to la-work-hard@yandex.ru'

from unittest.mock import patch

import const
from main import create_result, create_stat, create_time_stat, print_result


class TestMain:
    def test_create_result(self):
        const.host = 'ya.ru'
        const.arp = False
        assert create_result(2) == 'Connection to ya.ru: layer=network,' \
                                   ' port=80, tcp_seq=3' or 'Connection' \
                                                            ' timed out :('
        const.host = '192.168.0.8'
        const.arp = True
        assert create_result(3) == 'Connection to 192.168.0.8: ' \
                                   'layer=data link, arp_seq=4'

    def test_create_stat(self):
        const.passed, const.packages = 5, 10
        assert create_stat() == 'Packets: 5 (50%) passed, ' \
                                '5 (50%) failed, 10 sent'
        const.passed, const.packages = 3, 11
        assert create_stat() == 'Packets: 3 (28%) passed, ' \
                                '8 (72%) failed, 11 sent'

    def test_create_time_res(self):
        const.time = [14, 16, 20, 6]
        assert create_time_stat() == 'Packet sending time: min - 6 ms,' \
                                     ' max - 20 ms, average - 14.0 ms'
        const.time = [14.543, 20.765, 15.577, 18.431]
        assert create_time_stat() == 'Packet sending time: min - 14.543 ms,' \
                                     ' max - 20.765 ms, average - 17.329 ms'
        const.time = []
        assert create_time_stat() == 'Packets sending time: 0 ms'

    def test_print_result(self):
        const.mail = 'a.liza-2017@yandex.ru'
        const.host = 'google.com'
        const.arp = False
        assert print_result() == f'Successfully sent email to ' \
                                 f'a.liza-2017@yandex.ru'
        with patch('main.create_result'):
            const.mail = ''
            const.host = 'ya.ru'
            const.packages = 1
            const.passed = 0
            const.time = []
            assert print_result() == f'\n--ya.ru statistics--\nPackets: 0 ' \
                                     f'(0%) passed, 1 (100%) failed, 1 sent' \
                                     f'\nPackets sending time: 0 ms'

from unittest.mock import patch

import pytest

from constants import const
from main import create_result, create_stat, create_time_stat, print_result


class TestMain:
    test_result = [('ya.ru', False,
                    'Connection to ya.ru: layer=network, port=80, tcp_seq=3'),
                   ('192.168.0.8', True,
                    'Connection to 192.168.0.8: layer=data link, arp_seq=3')]

    @pytest.mark.parametrize('host, arp, result', test_result)
    def test_create_result(self, host, arp, result):
        const.host = host
        const.arp = arp
        assert create_result(2) == result

    test_stat = [(5, 10, 'Packets: 5 (50%) passed, 5 (50%) failed, 10 sent'),
                 (3, 11, 'Packets: 3 (28%) passed, 8 (72%) failed, 11 sent')]

    @pytest.mark.parametrize('passed, pack, result', test_stat)
    def test_create_stat(self, passed, pack, result):
        const.passed, const.packages = passed, pack
        assert create_stat() == result

    test_time = [([14, 16, 20, 6], 'Packet sending time: min - 6 ms,'
                                   ' max - 20 ms, average - 14.0 ms'),
                 ([14.543, 20.765, 15.577, 18.431],
                  'Packet sending time: min - 14.543 ms, max - 20.765 ms,'
                  ' average - 17.329 ms'),
                 ([], 'Packets sending time: 0 ms')]

    @pytest.mark.parametrize('time, result', test_time)
    def test_create_time_res(self, time, result):
        const.time = time
        assert create_time_stat() == result

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

    def test_print_impossible_result(self):
        const.mail = 'a.liza-2017@yandex.ru'
        const.host = 'google.com'
        const.arp = False
        const.packages = 'unlimited'
        with pytest.raises(SystemExit):
            print_result()

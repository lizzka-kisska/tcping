import pytest

from constants import const
from param_parser.getting_data import get_data, get_pack, \
    get_port, get_timeout, get_mail


class TestGettingData:
    args = [(['main.py', 'num=4'], 'num=4', False, 80, 1, 1, 0, ''),
            (['main.py', 'google.com', '-mail=a.liza-2017@yandex.ru'],
            'google.com', False, 80, 1, 1, 0, 'a.liza-2017@yandex.ru'),
            (['main.py', '192.168.0.8', '-port=45', '-num=10', '-tmt=6',
              '-lag=5', '-mail=a.liza-2017@yandex.ru'],
            '192.168.0.8', True, 45, 10, 6, 5, 'a.liza-2017@yandex.ru')]

    @pytest.mark.parametrize('args, host, arp, port, pack,'
                             ' tmt, lag, mail', args)
    def test_get_data(self, args, host, arp, port, pack, tmt, lag, mail):
        get_data(args)
        assert const.host == host
        assert const.arp == arp
        assert const.port == port
        assert const.packages == pack
        assert const.timeout == tmt
        assert const.delay == lag
        assert const.mail == mail

    @pytest.mark.parametrize('data, result', [(4, 4),
                                              ('unlimited', 'unlimited')])
    def test_get_pack(self, data, result):
        assert get_pack(data) == result

    def test_get_port(self):
        assert get_port(43) == 43

    def test_get_timeout(self):
        assert get_timeout(5) == 5

    mails = [('a.liza-2017@yandex.ru', 'a.liza-2017@yandex.ru'),
             ('resultping@ya.ru', 'resultping@ya.ru')]

    @pytest.mark.parametrize('data, result', mails)
    def test_get_mail(self, data, result):
        assert get_mail(data) == result

    wrong_args = [([]), (['main.py', 'asos.com', 'num', '=', '4']),
                  ['main.py', '-h'], ['main.py', '--help']]

    @pytest.mark.parametrize('data', wrong_args)
    def test_wrong_data(self, data):
        with pytest.raises(SystemExit):
            get_data(data)

    def test_wrong(self):
        with pytest.raises(SystemExit):
            get_pack(f'hi')
        with pytest.raises(SystemExit):
            get_port('4.3')
        with pytest.raises(SystemExit):
            get_port(78902)
        with pytest.raises(SystemExit):
            get_timeout('ya.ru')
        with pytest.raises(SystemExit):
            get_mail('a@google.com')
        with pytest.raises(SystemExit):
            get_mail('a')

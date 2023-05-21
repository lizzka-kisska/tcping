import pytest

from constants import const
from param_parser.getting_data import get_data, get_host, get_pack,\
    get_port, get_timeout, get_mail


class TestGettingData:
    test_data = [(['', 'num=4'], 'num=4', False, 80, 1, 1, 0, ''),
                 (['main.py', 'google.com', 'mail=a.liza-2017@yandex.ru'],
                  'google.com', False, 80, 1, 1, 0, 'a.liza-2017@yandex.ru'),
                 (['', '192.168.0.8', 'port=45', 'num=10', 'tmt=6', 'lag=5',
                   'mail=a.liza-2017@yandex.ru'],
                  '192.168.0.8', True, 45, 10, 6, 5, 'a.liza-2017@yandex.ru')]

    @pytest.mark.parametrize('args, host, arp, port, pack, tmt, lag, mail', test_data)
    def test_get_data(self, args, host, arp, port, pack, tmt, lag, mail):
        get_data(args)
        assert const.host == host
        assert const.arp == arp
        assert const.port == port
        assert const.packages == pack
        assert const.timeout == tmt
        assert const.delay == lag
        assert const.mail == mail

    test_host = [('8.8.8.8', '8.8.8.8'), ('ya.ru', 'ya.ru'),
                 ('ya.py', 'ya.py')]

    @pytest.mark.parametrize('data, result', test_host)
    def test_get_host(self, data, result):
        assert get_host(data) == result

    test_pack = [(4, 4), ('unlimited', 'unlimited')]

    @pytest.mark.parametrize('data, result', test_pack)
    def test_get_pack(self, data, result):
        assert get_pack(data) == result

    def test_get_port(self):
        assert get_port(43) == 43

    def test_get_timeout(self):
        assert get_timeout(5) == 5

    test_mail = [('a.liza-2017@yandex.ru', 'a.liza-2017@yandex.ru'),
                 ('resultping@ya.ru', 'resultping@ya.ru')]

    @pytest.mark.parametrize('data, result', test_mail)
    def test_get_mail(self, data, result):
        assert get_mail(data) == result

    def test_wrong_data(self):
        with pytest.raises(SystemExit):
            get_data([])
        with pytest.raises(SystemExit):
            get_data(['main.py', 'asos.com', 'num', '=', '4'])
        with pytest.raises(SystemExit):
            get_host('--help')
        with pytest.raises(SystemExit):
            get_host('-h')
        with pytest.raises(SystemExit):
            get_pack(f'hi')
        with pytest.raises(SystemExit):
            get_port('4.3')
        with pytest.raises(SystemExit):
            get_port(78902)
        with pytest.raises(SystemExit):
            get_timeout('ya.ru')

import pytest

import const
from getting_data import get_host, get_pack, get_port, get_timeout, get_data, get_mail


class TestGettingData:
    def test_get_data(self):
        get_data(['main.py', 'ya.ru'])
        assert const.host == 'ya.ru'
        get_data(['', 'num=4'])
        assert const.host == 'num=4'
        get_data(['main.py', 'google.com', 'mail=a.liza-2017@yandex.ru'])
        assert const.host == 'google.com'
        assert const.mail == 'a.liza-2017@yandex.ru'
        get_data(['', 'google.py', 'port=45', 'num=10', 'tmt=6', 'lag=5'])
        assert const.host == 'google.py'
        assert const.port == 45
        assert const.packages == 10
        assert const.timeout == 6
        assert const.delay == 5
        with pytest.raises(SystemExit):
            get_data([])
        with pytest.raises(SystemExit):
            get_data(['main.py', 'asos.com', 'num', '=', '4'])

    def test_get_host(self):
        assert get_host('ya.ru') == 'ya.ru'
        assert get_host('8.8.8.8') == '8.8.8.8'
        assert get_host('ya.py') == 'ya.py'
        with pytest.raises(SystemExit):
            get_host('--help')
        with pytest.raises(SystemExit):
            get_host('-h')

    def test_get_pack(self):
        assert get_pack(4) == 4
        assert get_pack('unlimited') == 'unlimited'
        with pytest.raises(SystemExit):
            get_pack(f'hi')

    def test_get_port(self):
        assert get_port(43) == 43
        with pytest.raises(SystemExit):
            get_port('4.3')
        with pytest.raises(SystemExit):
            get_port(78902)

    def test_get_timeout(self):
        assert get_timeout(5) == 5
        with pytest.raises(SystemExit):
            get_timeout('ya.ru')

    def test_get_mail(self):
        assert get_mail('a.liza-2017@yandex.ru') == 'a.liza-2017@yandex.ru'
        assert get_mail('resultping@ya.ru') == 'resultping@ya.ru'
        with pytest.raises(SystemExit):
            get_data('a.lizaaa2017@gmail.com')
        with pytest.raises(SystemExit):
            get_data('a.liza-2017yandex.ru')

import pytest

from getting_data import get_host, get_pack, get_port, get_timeout, get_data


class TestGettingData:
    def test_get_data(self):
        assert get_data(['main.py', 'ya.ru']) == ('ya.ru', 1, 80, 1, 0)
        assert get_data(['', 'num=4']) == ('num=4', 1, 80, 1, 0)
        assert get_data(['', 'google.com', 'port=45', 'num=10']) == ('google.com', 10, 45, 1, 0)
        assert get_data(['', 'ya.py', 'num=4', 'port=43', 'tmt=6', 'lag=5']) == ('ya.py', 4, 43, 6, 5)
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

import pytest

from connection_socket import plug_socket


class TestConnSocket:
    def test_plug_socket(self):
        assert plug_socket('ya.ru', 80, 1, 5) == ('Connection to ya.ru:'
                                                  ' layer=network, port=80,'
                                                  ' tcp_seq=6', 1)
        assert plug_socket('8.8.8.8', 53, 1, 1) == ('Connection to 8.8.8.8:'
                                                    ' layer=network, port=53,'
                                                    ' tcp_seq=2', 1)
        assert plug_socket('8.8.8.8', 80, 1, 1) == ('Connection '
                                                    'timed out :(', 0)
        with pytest.raises(SystemExit):
            plug_socket('ya.py', 80, 1, 1)

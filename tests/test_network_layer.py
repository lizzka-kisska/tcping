import pytest

from connection.network_layer import send_packet


class TestConnSocket:
    test_data = [('ya.ru', 80, 1, 5,
                  'Connection to ya.ru: layer=network, port=80, tcp_seq=6'),
                 ('8.8.8.8', 53, 1, 1,
                  'Connection to 8.8.8.8: layer=network, port=53, tcp_seq=2'),
                 ('8.8.8.8', 80, 1, 1, 'Connection timed out :(')]

    @pytest.mark.parametrize('host, port, tmt, num, result', test_data)
    def test_send_packet(self, host, port, tmt, num, result):
        assert send_packet(host, port, tmt, num)[0] == result

    def test_send_wrong_packet(self):
        with pytest.raises(SystemExit):
            send_packet('ya.py', 80, 1, 1)

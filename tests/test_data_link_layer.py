import pytest

from connection.data_link_layer import send_frame


class TestConnArp:
    test_data = [('192.168.0.1', 1, 2,
                  'Connection to 192.168.0.1: layer=data link, arp_seq=3'),
                 ('192.168.254.254', 1, 2, f'Connection timed out :(')]

    @pytest.mark.parametrize('host, tmt, num, result', test_data)
    def test_send_frame(self, host, tmt, num, result):
        assert send_frame(host, tmt, num)[0] \
               == result

    def test_send_wrong_frame(self):
        with pytest.raises(SystemExit):
            send_frame('192.168.256.256', 1, 2)

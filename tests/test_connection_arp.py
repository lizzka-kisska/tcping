import pytest

from connection_arp import send_frame


class TestConnArp:
    def test_plug_arp_host(self):
        assert send_frame('192.168.0.8', 1, 2)[0] \
               == 'Connection to 192.168.0.8: layer=data link, arp_seq=3'
        assert send_frame('192.168.254.254', 1, 2)[0] == f'Connection timed out :('
        with pytest.raises(SystemExit):
            send_frame('192.168.256.256', 1, 2)

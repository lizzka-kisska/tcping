from connection_arp import plug_arp_host


class TestConnArp:
    def test_plug_arp_host(self):
        assert plug_arp_host('192.168.0.2', 1, 2) == \
               (f'Connection to 98:52:3d:45:01:c4: tcp_seq=3', 1)
        assert plug_arp_host('10.10.0.5', 1, 3) == \
               (f'Connection timed out :(', 0)

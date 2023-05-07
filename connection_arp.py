import timeit

import scapy.all as scapy
from scapy.layers.l2 import Ether, ARP

import const


def plug_arp_host(host, timeout, seq):
    try:
        arp_request = ARP(pdst=host)
        broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request
        start_time = timeit.default_timer()
        # отправить пакет на канальном (L2) уровне
        answer = scapy.srp(arp_request_broadcast, timeout=timeout,
                           verbose=False)[0]
        res_time = (timeit.default_timer() - start_time) * 1000
        const.time.append(float(format(res_time, '.3f')))
        if answer.sessions():
            return f'Connection to {answer[0][1].hwsrc}: tcp_seq={seq+1}', 1
        else:
            return f'Connection timed out :(', 0
    except scapy.Scapy_Exception:
        return f'Something gone wrong'

    # answer.summary()

    # print(answer.sessions())
    # print(answer[0][1])

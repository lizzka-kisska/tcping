import socket
import struct
import sys
import time
import timeit

import pcap

import const


def send_frame(host, timeout, seq):
    try:
        # Создание заголовка Ethernet для ARP-запроса
        dst_mac = b"\xff\xff\xff\xff\xff\xff"  # Широковещательный MAC-адрес
        src_mac = b"\x50\xde\x06\xb9\x64\x64"  # MAC-адрес отправителя
        eth_type = b"\x08\x06"  # ARP
        eth_hdr = struct.pack("!6s6s2s", dst_mac, src_mac, eth_type)

        # Создание заголовка ARP для ARP-запроса
        eth_code = b"\x00\x01"  # Ethernet
        ip_code = b"\x08\x00"  # IPv4
        mac_len = b"\x06"  # Длина MAC-адреса (6 байт)
        ip_len = b"\x04"  # Длина IP-адреса (4 байта)
        op = b"\x00\x01"  # ARP-запрос

        sender_mac = src_mac
        sender_ip = socket.inet_aton(
            socket.gethostbyname(socket.gethostname()))
        target_mac = b"\x00\x00\x00\x00\x00\x00"  # Неизвестный MAC получателя
        target_ip = socket.inet_aton(host)  # IP-адрес получателя
        arp_hdr = struct.pack("!2s2s1s1s2s6s4s6s4s", eth_code, ip_code,
                              mac_len, ip_len, op, sender_mac, sender_ip,
                              target_mac, target_ip)
        pcap_obj = pcap.pcap("en0", immediate=True)
        packet = eth_hdr + arp_hdr

        try:
            pcap_obj.sendpacket(packet)
            start_run = time.time()
            while True:
                result = unpack_and_find_result(pcap_obj, sender_ip,
                                                target_ip, seq)
                if result:
                    return result
                elif time.time() - start_run >= timeout:
                    return f'Connection timed out :(', 0
        finally:
            pcap_obj.close()
    except OSError:
        print('You have entered the ip incorrectly')
        sys.exit(0)


def unpack_and_find_result(frame, sender_ip, target_ip, seq):
    start_time = timeit.default_timer()
    packet_data = frame.__next__()[1]
    ethernet_type = struct.unpack("!6s6s2s", packet_data[:14])[2]
    # TODO обработка неправильного ip
    if ethernet_type == b"\x08\x06":  # ARP
        unpacked_pack = struct.unpack("!2s2s1s1s2s6s4s6s4s",
                                      packet_data[14:42])
        arp_op, arp_sender_ip, arp_target_ip = unpacked_pack[4], \
            unpacked_pack[6], unpacked_pack[8]
        if arp_op == b"\x00\x02" and arp_target_ip == sender_ip\
                and arp_sender_ip == target_ip:
            res_time = (timeit.default_timer() - start_time) * 1000
            const.time.append(float(format(res_time, '.3f')))
            return f'Connection to {socket.inet_ntoa(arp_sender_ip)}: ' \
                   f'layer=data link, arp_seq={seq+1}', 1

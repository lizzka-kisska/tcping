# Создание заголовка Ethernet для ARP-запроса
dst_mac = b'\xff\xff\xff\xff\xff\xff'  # Широковещательный MAC-адрес
src_mac = b'\x50\xde\x06\xb9\x64\x64'  # MAC-адрес отправителя
eth_type = b'\x08\x06'  # ARP

# Создание заголовка ARP для ARP-запроса
eth_code = b'\x00\x01'  # Ethernet
ip_code = b'\x08\x00'  # IPv4
mac_len = b'\x06'  # Длина MAC-адреса (6 байт)
ip_len = b'\x04'  # Длина IP-адреса (4 байта)
op_request = b'\x00\x01'  # ARP-запрос
op_answer = b'\x00\x02'

target_mac = b'\x00\x00\x00\x00\x00\x00'  # Неизвестный MAC получателя

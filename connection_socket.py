import socket
import sys
import timeit

import const


def plug_socket(host, port, timeout, seq):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # апв4, тсп
    s.settimeout(timeout)
    try:
        start_time = timeit.default_timer()
        s.connect((host, int(port)))
        res_time = (timeit.default_timer() - start_time) * 1000
        const.time.append(float(format(res_time, '.3f')))
        s.shutdown(socket.SHUT_RD)
        s.close()
        return f'Connection to {host}: layer=network, port={port}, tcp_seq={seq+1}', 1
    # TODO ConnectionRefusedError:
    except socket.timeout:
        return f'Connection timed out :(', 0
    except socket.gaierror:
        print(f'You may have entered the domain or ip incorrectly')
        sys.exit(0)

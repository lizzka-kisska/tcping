import sys
import time
import warnings

import const
from connection_arp import plug_arp_host
from connection_socket import plug_socket
from getting_data import get_data
from sending_mail import send_mail


def create_result(count):
    if not const.arp or const.arp.lower() == 'no' or const.arp.lower() == 'n':
        result, success = \
            plug_socket(const.host, const.port, const.timeout, count)
    else:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=DeprecationWarning)
            result, success = plug_arp_host(const.host, const.timeout, count)
    const.passed += success
    return result


def create_stat():
    failed = const.packages - const.passed
    stat_f = int(failed / const.packages * 100)
    stat_p = 100 - stat_f
    return f'Packets: {const.passed} ({stat_p}%) passed, {failed} ' \
           f'({stat_f}%) failed, {const.packages} sent'


def create_time_stat():
    time_res = const.time
    if time_res:
        min_time = min(time_res)
        average_time = sum(time_res) / len(time_res)
        max_time = max(time_res)
        return f'Packet sending time: min - {min_time} ms, max - {max_time}' \
               f' ms, average - {int(average_time * 1000) / 1000} ms'
    else:
        return 'Packets sending time: 0 ms'


def print_result():
    if not sys.argv[0].startswith('/Users'):
        get_data(sys.argv)
    const.passed = 0
    count = 0
    result = ''
    if str(const.packages).isalpha():
        while True:
            if not const.mail:
                print('It is impossible to send the result to the mail')
            print(create_result(count))
            count += 1
    else:
        while count < const.packages:
            line_result = create_result(count)
            if not const.mail:
                time.sleep(const.delay)
                print(line_result)
            result += line_result + f'\n'
            count += 1

    result_stat = f'\n--{const.host} statistics--' + f'\n'
    result_stat += create_stat() + f'\n'
    result_stat += create_time_stat()
    if const.mail:
        return send_mail(result + result_stat)
    else:
        return result_stat


if __name__ == '__main__':
    print(print_result())

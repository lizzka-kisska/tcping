import sys
import time

from constants import const
from connection.data_link_layer import send_frame
from connection.network_layer import send_packet
from mail.sending_mail import send_mail
from param_parser.getting_data import get_data


def create_result(count):
    if const.arp:
        result, success = \
            send_frame(const.host, const.timeout, count)
    else:
        result, success = send_packet(const.host, const.port, const.timeout, count)
    const.passed += success
    return result


def create_stat():
    failed = const.packages - const.passed
    stat_f = int(failed / const.packages * const.percent_100)
    stat_p = const.percent_100 - stat_f
    return f'Packets: {const.passed} ({stat_p}%) passed, {failed} ' \
           f'({stat_f}%) failed, {const.packages} sent'


def create_time_stat():
    time_res = const.time
    if time_res:
        min_time = min(time_res)
        average_time = sum(time_res) / len(time_res)
        max_time = max(time_res)
        return f'Packet sending time: min - {min_time} ms, max - {max_time}' \
               f' ms, average - {average_time:.3f} ms'
    else:
        return 'Packets sending time: 0 ms'


def get_and_print_result():
    get_data(sys.argv)
    const.passed = 0
    count = 0
    result = ''
    if str(const.packages).isalpha():
        while True:
            if const.mail:
                print('It is impossible to send the result to the mail')
                sys.exit(0)
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
    print(get_and_print_result())

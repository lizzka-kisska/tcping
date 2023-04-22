import sys
import time

import const
from connection_socket import plug_socket
from getting_data import get_data


def create_result(count):
    result, success = \
        plug_socket(const.host, const.port, const.timeout, count)
    const.passed += success
    time.sleep(const.delay)
    return result


def create_stat():
    failed = const.packages - const.passed
    stat_f = int(failed / const.packages * 100)
    stat_p = 100 - stat_f
    return 'Packages: {} ({}%) passed, {} ({}%) failed, {} sent'. \
        format(const.passed, stat_p, failed, stat_f, const.packages)


def create_time_stat():
    time_res = const.time
    if time_res:
        min_time = min(time_res)
        average_time = sum(time_res) / len(time_res)
        max_time = max(time_res)
        return 'Package sending time: ' \
               'min - {} ms, max - {} ms, average - {} ms'\
            .format(min_time, max_time, int(average_time * 1000) / 1000)
    else:
        return 'Package sending time: 0 ms'


def main():
    if not sys.argv[0].startswith('/Users'):
        const.host, const.packages, const.port, const.timeout, const.delay = \
            get_data(sys.argv)
    const.passed = 0
    count = 0
    if str(const.packages).isalpha():
        while True:
            print(create_result(count))
            count += 1
    else:
        while count < const.packages:
            print(create_result(count))
            count += 1

    print('\n--{} statistics--'.format(const.host))
    print(create_stat())
    print(create_time_stat())


if __name__ == '__main__':
    main()

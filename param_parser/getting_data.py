import argparse
import sys

from constants import const


def get_data(data):
    parser = argparse.ArgumentParser(description='Ping')
    parser.add_argument('host', help='server or IP address')
    parser.add_argument('-num', help='number of packages(number or "unlimited")', default=1)
    parser.add_argument('-port', help='port number', default=80)
    parser.add_argument('-tmt', help='timeout', default=1)
    parser.add_argument('-lag', help='delay', default=0)
    parser.add_argument('-mail', help='yandex email address', default='')
    args = parser.parse_args(data[1:])

    const.host = args.host
    get_protocol(args.host)
    const.packages = get_pack(args.num)
    const.port = get_port(args.port)
    const.timeout = get_timeout(args.tmt)
    const.delay = get_timeout(args.lag)
    const.mail = get_mail(args.mail) if args.mail != '' else ''


def get_pack(data):
    try:
        return data if data == 'unlimited' else int(data)
    except ValueError:
        print(f'Number of packages must be a number or "unlimited"')
        sys.exit(0)


def get_port(data):
    try:
        res = int(data)
        if res <= 65535:
            return res
        else:
            raise ValueError
    except ValueError:
        print(f'Port must be a number: 43, 80 or 1024<number<65535')
        sys.exit(0)


def get_timeout(data):
    try:
        return int(data)
    except ValueError:
        print(f'Timeout must be a number')
        sys.exit(0)


def get_mail(data):
    if data.find('@') != -1:
        if data.split('@')[1].startswith('ya'):
            return data
        else:
            print(f'Your mail must have a yandex domain')
            sys.exit(0)
    else:
        print(f'Email must be ...@ + yandex domain')
        sys.exit(0)


def get_protocol(host):
    if host.isalpha():
        const.arp = False
    else:
        ip = host.split('.')
        if ip[0] == '10' or (ip[0] == '192' and ip[1] == '168') or \
                (ip[0] == '172' and 16 <= int(ip[1]) < 32) or \
                (ip[0] == 100 and 64 <= int(ip[1]) < 128):
            const.arp = True
        else:
            const.arp = False

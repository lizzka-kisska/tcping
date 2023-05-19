import sys

import const


def get_data(args):
    try:
        const.host = get_host(args[1])
        get_proto(const.host)
    except IndexError:
        print(f'You must enter the domain name or ip address')
        sys.exit(0)
    try:
        for i in range(2, 7):
            command, data = args[i].split('=')
            if command == 'num':
                const.packages = get_pack(data)
            elif command == 'port':
                const.port = get_port(data)
            elif command == 'tmt':
                const.timeout = get_timeout(data)
            elif command == 'lag':
                const.delay = get_timeout(data)
            elif command == 'mail':
                const.mail = get_mail(data)
    except IndexError:
        pass
    except ValueError:
        print(f'You must use num=..., port=..., timeout=..., '
              f'lag=..., mail=...')
        sys.exit(0)


def get_host(data):
    if data == '--help' or data == '-h':
        print(
            f'With this program, you can ping the server or IP address, '
            f'to do this, enter:\n'
            f' * server / IP address\n'
            f' * num=number of packages(number or "unlimited")\n'
            f' * port=port number\n'
            f' * tmt=timeout\n'
            f' * lag=delay\n'
            f' * mail=email address')
        sys.exit(0)
    else:
        return str(data)


def get_pack(data):
    try:
        if data == f'unlimited':
            return data
        else:
            return int(data)
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


def get_proto(host):
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

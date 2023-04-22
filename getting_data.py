import sys

import const

packages = 1
port = 80
timeout = 1
delay = 0


def get_data(args):
    global packages, port, timeout, delay
    try:
        host = get_host(args[1])
    except IndexError:
        print(f'You must enter the domain name or ip address')
        sys.exit(0)
    try:
        for i in range(2, 6):
            command, data = args[i].split('=')
            match command:
                case 'num':
                    packages = get_pack(data)
                case 'port':
                    port = get_port(data)
                case 'tmt':
                    timeout = get_timeout(data)
                case 'lag':
                    delay = get_timeout(data)
    except IndexError:
        pass
    except ValueError:
        print(f'You must use num=..., port=..., timeout=...')
        sys.exit(0)
    return host, packages, port, timeout, delay


def get_host(data):
    if data == '--help' or data == '-h':
        print(
            f'With this program, you can ping the server or IP address, '
            f'to do this, enter:\n'
            f' * server / IP address\n'
            f' * num=number of packages(number or "unlimited")\n'
            f' * port=port number\n'
            f' * tmt=timeout\n'
            f' * lag=delay')
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
    except IndexError:
        pass


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
    except IndexError:
        pass


def get_timeout(data):
    try:
        return int(data)
    except ValueError:
        print(f'Timeout must be a number')
        sys.exit(0)
    except IndexError:
        pass

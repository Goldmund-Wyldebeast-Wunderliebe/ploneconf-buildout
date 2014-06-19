
tst = {
    'hosts': ['app-fabric-tst@cobain.gw20e.com'],
    'instances': { 'ports': { 'instance0': 8196, }, },
    'credentials': { 'username': 'app-fabric-tst', 'password': 'keuteltje14', },
}

acc = {
    'hosts': ['app-fabric-acc@cobain.gw20e.com'],
    'haproxy': { 'port': 21895 },
    'zeo': { 'port': 18195, 'base': '/opt/APPS/fabric/acc/db', },
    'instances': {
        'ports': { 'instance0': 8195, },
        'ipaddresses': { 'localhost': '127.0.0.1', },
    },
    'flyingip': '127.0.0.1',
    'credentials': { 'username': 'app-fabric-acc', 'password': 'keuteltje14', },
}

prd = {
    'hosts': [
        'app-fabric-prd@192.168.5.52',
        'app-fabric-prd@192.168.5.53',
    ],
    'varnish': { 'port': 48450 },
    'haproxy': { 'port': 28450 },
    'zeo': { 'port': 18450, 'base': '/data1/APPS/fabric/prd' },
    'instances': {
        'ports': {'instance{}'.format(i): 8450+i for i in range(4)},
        'ipaddresses': { 'madras': '192.168.5.52', 'saag': '192.168.5.53', },
    },
    'flyingip': '91.194.224.154',
    'credentials': { 'username': 'app-fabric-prd', 'password': 'keuteltje14', },
    'sentry': {
        'dsn': 'https://sentry_api_key:example@sentry.gw20e.com/xx',
        'level': 'ERROR',
    },
}


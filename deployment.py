
tst = dict(
    hosts= ['app-fabric-tst@cobain.gw20e.com'],
    buildout= 'buildout-tst',
    instances= { 'ports': { 'instance0': 8194, }, },
    credentials= { 'username': 'app-fabric-tst', 'password': 'keuteltje14', },
    webserver= 'apache2',
    sitename= 'tst.example.com',
)

acc = dict(
    hosts= ['app-fabric-acc@cobain.gw20e.com'],
    buildout= 'buildout-acc',
    haproxy= { 'port': 21895 },
    zeo= { 'port': 18195, 'base': '/opt/APPS/fabric/acc/db', },
    instances= {
        'ports': { 'instance0': 8195, 'instance1': 8196, },
        'ipaddresses': { 'localhost': '127.0.0.1', },
    },
    credentials= { 'username': 'app-fabric-acc', 'password': 'keuteltje14', },
    webserver= 'apache2',
    sitename= 'acc.example.com',
)


def _datestamped(fmt):
    from datetime import datetime
    now = datetime.now()
    return now.strftime(fmt)

prd = dict(
    hosts= [
        'app-fabric-prd@192.168.5.52',
        'app-fabric-prd@192.168.5.53',
    ],
    buildout= _datestamped('releases/%Y-%m-%d'),
    zeo= {
        'ip': '91.194.224.154',
        'port': 18450,
    },
    instances= {
        'ports': {'instance{}'.format(i): 8450+i for i in range(4)},
        'ipaddresses': { 'madras': '192.168.5.52', 'saag': '192.168.5.53', },
    },
    credentials= { 'username': 'app-fabric-prd', 'password': 'keuteltje14', },
    sentry= {
        'dsn': 'https://sentry_api_key:example@sentry.gw20e.com/xx',
        'level': 'ERROR',
    },
)

prdbe = prd.copy()
prdbe.update(
    buildout= 'releases/backend',
    zeo = dict(base= '/data1/APPS/fabric/prd', **prd['zeo']),
)

prdfe = prd.copy()
prdfe.update(
    buildout= 'releases/frontend',
    varnish= { 'port': 48450 },
    haproxy= { 'port': 28450 },
    webserver= 'apache2',
    sitename= 'www.example.com',
)


default = tst


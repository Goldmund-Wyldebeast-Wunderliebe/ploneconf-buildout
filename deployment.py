
tst = dict(
    hosts= ['app-fabric-acc@cobain.gw20e.com'],
    buildout= 'buildout-tst',
    modules = {
        'gww.imprint': 'git git@git.gw20e.com:gww/gww-imprint.git',
    },
    instances= { 'ports': { 'instance0': 8194, }, },
    credentials= { 'username': 'app-fabric-tst', 'password': 'keuteltje14', },
    site_id = 'mysite',
    webserver= 'apache2',
    sitename= 'fabric-tst.gw20e.com',
)

acc = dict(
    hosts= ['app-fabric-acc@cobain.gw20e.com'],
    buildout= 'buildout-acc',
    haproxy= { 'port': 28195 },
    zeo= { 'port': 18195, 'base': '/opt/APPS/fabric/acc/db', },
    instances= {
        'ports': { 'instance0': 8195, 'instance1': 8196, },
        'ipaddresses': { 'localhost': '127.0.0.1', },
    },
    credentials= { 'username': 'app-fabric-acc', 'password': 'keuteltje14', },
    site_id = 'mysite',
    webserver= 'apache2',
    sitename= 'fabric-acc.gw20e.com',
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
    current_link = 'current',
    auto_switch = False,
    zeo= {
        'ip': '91.194.224.154',
        'port': 18450,
    },
    instances= {
        'ports': {'instance{}'.format(i): 8450+i for i in range(4)},
        'ipaddresses': { 'madras': '192.168.5.52', 'saag': '192.168.5.53', },
    },
    site_id = 'mysite',
    credentials= { 'username': 'app-fabric-prd', 'password': 'keuteltje14', },
    sentry= {
        'dsn': 'https://sentry_api_key:example@sentry.gw20e.com/xx',
        'level': 'ERROR',
    },
)

prdfe = dict(
    hosts = prd['hosts'],
    buildout= 'releases/frontend',
    varnish= { 'port': 48450 },
    haproxy= { 'port': 28450, 'instances': prd['instances'], },
    webserver= 'apache2',
    sitename= 'fabric-www.gw20e.com',
    site_id = 'mysite',
)

prdbe = dict(
    hosts = prd['hosts'],
    buildout= 'releases/backend',
    zeo = dict(base= '/data1/APPS/fabric/prd', **prd['zeo']),
)


default = 'tst'


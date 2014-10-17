_base_port = 8080
_env_name = 'testapp'
_site_id = 'Plone'

_flying_ip = 'ploneconf.puppet'
_servers = {'ploneconf': 'ploneconf.puppet'}

_modules = {
    'gww.imprint': 'git https://github.com/Goldmund-Wyldebeast-Wunderliebe/gww.imprint.git',
}

_third_party_modules = {
    # 'collective.autopublishing': 'git https://github.com/collective/collective.autopublishing.git',
}

def _datestamped(fmt):
    from datetime import datetime
    now = datetime.now()
    return now.strftime(fmt)

tst = dict(
    hosts=['app-%s-tst@%s' % (_env_name, s) for s in _servers.values()],
    buildout='buildout-tst',
    haproxy={'port': _base_port + 20002},
    modules=_modules,
    third_party_modules=_third_party_modules,
    zeo={
        'ip': _flying_ip,
        'port': _base_port + 20001,
        'base': '/opt/APPS/%s/tst/db' % _env_name,
    },
    instances={
        'ports': {'instance0': _base_port + 2, },
        'ipaddresses': _servers,
    },
    credentials={'username': 'admin', 'password': 'secret', },
    site_id=_site_id,
    webserver='apache2',
    sitename='%s-tst.gw20e.com' % _env_name,
    remote_configs={'clockusers': 'clockuser.cfg'},
)

acc = dict(
    hosts=['app-%s-acc@%s' % (_env_name, s) for s in _servers.values()],
    buildout='buildout-acc',
    haproxy={'port': _base_port + 30002},
    modules=_modules,
    third_party_modules=_third_party_modules,
    zeo={
        'ip': _flying_ip,
        'port': _base_port + 30001,
        'base': '/opt/APPS/%s/acc/db' % _env_name,
    },
    instances={
        'ports': {'instance0': _base_port + 3, 'instance1': _base_port + 4, },
        'ipaddresses': _servers,
    },
    credentials={'username': 'admin', 'password': 'secret', },
    site_id=_site_id,
    webserver='apache2',
    sitename='%s-acc.gw20e.com' % _env_name,
    remote_configs={'clockusers': 'clockuser.cfg'},
)

prd = dict(
    hosts=['app-%s-prd@%s' % (_env_name, s) for s in _servers.values()],
    buildout=_datestamped('releases/%Y-%m-%d'),
    current_link='current',
    auto_switch=False,
    modules=_modules,
    third_party_modules=_third_party_modules,
    zeo={
        'ip': _flying_ip,
        'port': _base_port + 40001,
    },
    instances={
        'ports': {'instance{}'.format(i): _base_port + 5 + i for i in range(4)},
        'ipaddresses': _servers,
    },
    site_id=_site_id,
    credentials={'username': 'admin', 'password': 'secret', },
    remote_configs={'clockusers': 'clockuser.cfg'},
    sentry={
        'dsn': 'https://406ca4faab4b4dfd9c40f5ff790d5294:012c8b89ccb4420582d38d474c26cd11@sentry.gw20e.com/29',
        'level': 'ERROR',
    },
)

prdfe = dict(
    hosts=prd['hosts'],
    buildout='releases/frontend',
    varnish={'port': _base_port + 40003},
    haproxy={'port': _base_port + 40002, 'instances': prd['instances'], },
    webserver='apache2',
    sitename='%s-prd.gw20e.com' % _env_name,
    site_id=prd['site_id'],
)

prdbe = dict(
    hosts=prd['hosts'],
    buildout='releases/backend',
    zeo=dict(base='/data1/APPS/%s/prd' % _env_name, **prd['zeo']),
)

default = 'tst'

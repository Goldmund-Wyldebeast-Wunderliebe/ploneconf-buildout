_env_name = 'hhd'

from base.deployment import (_flying_ip, _servers, _modules, _third_party_modules,
    templates)

_base_port = 8210
# tst instances use _base_port +1
#     zeo uses                 +10001
#     haproxy uses             +10002
# acc instances use _base_port +2, +3 (instances)
#     zeo uses                 +10002
#     haproxy uses             +20002
# prd instances use _base_port +4 ... +7
#     zeo uses                 +10004
#     haproxy uses             +20004
#     varnish uses             +40004

_modules.update({
    'hhd.theme.intranet': 'git git@git.gw20e.com:waterschappen/hhd-theme-intranet.git',
    'hhd.theme.internet': 'git git@git.gw20e.com:waterschappen/hhd-theme-internet.git',
})

tst = dict(
    hosts= ['app-%s-tst@%s' % (_env_name, s) for s in _servers.values()],
    buildout= 'buildout-tst',
    haproxy= { 'port': _base_port + 10001 },
    modules = _modules,
    third_party_modules = _third_party_modules,
    zeo= {
        'ip': _flying_ip,
        'port': _base_port + 10001,
        'base': '/opt/APPS/%s/tst/db' % _env_name,
    },
    instances= {
        'ports': { 'instance0': _base_port+1, },
        'ipaddresses': _servers,
    },
    credentials= { 'username': 'admin', 'password': 'secret', },
    site_id = 'intranet',
    webserver= 'apache2',
    sitename= '%s-tst.gw20e.com' % _env_name,
    clockserver_user= 'clocktestuser',
    clockserver_password= 'clocktestpassword',
    sitetypes= ('intranet', 'internet'),
)

acc = dict(
    hosts= ['app-%s-acc@%s' % (_env_name, s) for s in _servers.values()],
    buildout= 'buildout-acc',
    haproxy= { 'port': _base_port + 20002 },
    zeo= {
        'ip': _flying_ip,
        'port': _base_port + 10002,
        'base': '/opt/APPS/%s/acc/db' % _env_name,
    },
    instances= {
        'ports': { 'instance0': _base_port + 2, 'instance1': _base_port + 3, },
        'ipaddresses': _servers,
    },
    credentials= { 'username': 'admin', 'password': 'secret', },
    site_id = 'mysite',
    webserver= 'apache2',
    sitename= '%s-acc.gw20e.com' % _env_name,
)


def _datestamped(fmt):
    from datetime import datetime
    now = datetime.now()
    return now.strftime(fmt)

prd = dict(
    hosts= ['app-%s-prd@%s' % (_env_name, s) for s in _servers.values()],
    buildout= _datestamped('releases/%Y-%m-%d'),
    current_link = 'current',
    auto_switch = False,
    zeo= {
        'ip': _flying_ip,
        'port': _base_port + 10004,
    },
    instances= {
        'ports': {'instance{}'.format(i): _base_port + 4 + i for i in range(4)},
        'ipaddresses': _servers,
    },
    site_id = 'mysite',
    credentials= { 'username': 'admin', 'password': 'secret', },
    sentry= {
        'dsn': 'https://sentry_api_key:example@sentry.gw20e.com/xx',
        'level': 'ERROR',
    },
)

prdfe = dict(
    hosts = prd['hosts'],
    buildout= 'releases/frontend',
    varnish= { 'port': _base_port + 40004 },
    haproxy= { 'port': _base_port + 20004, 'instances': prd['instances'], },
    webserver= 'apache2',
    sitename= '%s-prd.gw20e.com' % _env_name,
    site_id = 'mysite',
)

prdbe = dict(
    hosts = prd['hosts'],
    buildout= 'releases/backend',
    zeo = dict(base= '/data1/APPS/%s/prd' % _env_name, **prd['zeo']),
)


default = 'tst'

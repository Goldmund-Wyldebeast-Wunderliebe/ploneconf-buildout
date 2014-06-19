""" GWW Fabric file for Plone buildouts

This file can be changed to meet the needs of a specific buildout. The Git
submodule `fabric_lib` has generic functions to provision buildout
environments.

To activate the fabric_lib submodule::

  git submodule init
  git submodule update

Fabric uses SSH to send commands to a Appie user. Make sure you create an
SSH connection to the Appie user. For more info see 'Preparing Appie
environments' in the docs (./fabric_lib/README.rst).

Usage::

  ./bin/fab <fabric command>:<optional parameter>

"""

import git
from fabric.api import env


try:
    from fabric_lib.tasks import (
            check_cluster, test, update, deploy, switch, copy,
            prepare_release,
            )
except ImportError:
    print('To activate the fabric_lib submodule run:\n'
          '  git submodule init && git submodule update\n'
          'For more info read https://intranet.gw20e.com/development/plone-projecten/fabric-deployment'
    )
    import fabric_lib.tasks  # Just to show the real error message
    exit(0)


#############
# Env config
#############
env.forward_agent = True
env.always_use_pty = False
env.linewise = True


##############
# Appie config
# CHANGE THE FOLLOWING VARIABLES FOR YOUR BUILDOUT / APPIE ENV:
##############
env.app = 'fabric'  # Name of the appie environment
env.modules = ('project.egg', )  # Module which can be updated using git pull
env.site_url = 'http://localhost:{0}/plone_id/'  # Local url to Plone
env.buildout_uri = git.Repo().remote().url  # Git uri to buildout
env.deploy_info = {  # SSH uri's for acc and prd
    'acc': {
        'hosts': ['app-{0}-acc@cobain.gw20e.com'.format(env.app)],
        'ports': {
            'haproxy': 21895,
            'instances': {'instance0': 8195},
            'zeo': 18195,
        },
        'ipaddresses': {
            'flying-ip': '127.0.0.1',
            'ip-one': '127.0.0.1',
        },
        'credentials': {
            'username': 'app-{}-acc'.format(env.app),
            'password': 'keuteltje14',
        },
        'zeo-base': '/opt/APPS/{}/acc/db'.format(env.app),
        'buildout-parts': {
            'sentry': {
                'dsn': 'https://sentry_api_key:example@sentry.gw20e.com/xx',
                'level': 'ERROR',
            },
        },
    },
    'prd': {
        'hosts': [
            'app-{0}-prd@192.168.5.52'.format(env.app),
            'app-{0}-prd@192.168.5.53'.format(env.app),
        ],
        'ports': {
            'varnish': 48450,
            'haproxy': 28450,
            'instances': {'instance{}'.format(i): 8450+i for i in range(4)},
            'zeo': 18450,
        },
        'ipaddresses': {
            'flying-ip': '91.194.224.154',
            'ip-one': '192.168.5.52', # Madras
            'ip-two': '192.168.5.53', # Saag
        },
        'credentials': {
            'username': 'app-{}-prd'.format(env.app),
            'password': 'keuteltje14',
        },
        'zeo-base': '/data1/APPS/fabric/prd',
        'buildout-parts': {
            'sentry': {
                'dsn': 'https://sentry_api_key:example@sentry.gw20e.com/xx',
                'level': 'ERROR',
            },
            'supervisor': {
                'user': 'admin',
                'password': 'ev9OpeeT',
            },
        },
    },
}

try:
   import localfabfile
except ImportError:
    pass

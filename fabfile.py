""" GWW Fabric file for Plone buildouts

This file can be changed to meet the needs of a specific buildout. The Git
submodule `fabric_lib` has generic functions to provision buildout
environments.

To active the fabric_lib submodule::

  git submodule init
  git submodule update

Fabric uses SSH to send commands to a Appie user. Make sure you create a
SSH connection to the Appie user. For more info see 'Preparing Nuffic Appie
environments' in the docs (./fabric_lib/README.rst).

Usage::

  ./bin/fab <fabric command>:<optional parameter>

"""

import git
from fabric.api import env
from fabric.decorators import task


try:
    from fabric_lib.tasks import (
            check_cluster, test, update, deploy, switch, copy,
            )
except ImportError:
    print('To active the fabric_lib submodule run:\n'
          '  git submodule init && git submodule update\n'
          'For more info read https://intranet.gw20e.com/development/plone-projecten/fabric-deployment'
    )
    import fabric_lib.tasks  # Just to show the real error message
    exit(0)


##############
# Appie config
##############

# CHANGE THE FOLLOWING VARIABLES FOR YOUR BUILDOUT / APPIE ENV:

# Name of the appie environment
env.app = 'fabric'
# Module which can be updated using git pull
env.modules = ('project.egg', )
# Local url to Plone
env.site_url = 'http://localhost:{0}/plone_id/'
# Git uri to buildout
env.buildout_uri = git.Repo().remote().url
# SSH uri's for acc and prd
env.deploy_info = {
    'acc': {
        'hosts': ['app-{0}-acc@cobain.gw20e.com'.format(env.app)],
    },
    'prd': {
        'hosts': [
            'app-{0}-prd@192.168.5.52'.format(env.app),
            'app-{0}-prd@192.168.5.53'.format(env.app),
        ],
    },
}


#############
# Env config
#############
env.forward_agent = True
env.always_use_pty = False
env.linewise = True


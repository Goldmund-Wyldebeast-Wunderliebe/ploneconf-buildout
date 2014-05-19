""" GWW Fabric file for Plone buildouts

This file can be changed to meet the needs of a specific buildout. The Git
submodule `fabric_lib` has generic functions to provision buildout 
environments.

To active the fabric_lib submodule::

  git submodule init
  git submodule update

Fabric uses SSH to send commands to a Appie user. Make sure you create a 
SSH connection to the Appie user. For more info see 'Prepairing Nuffic Appie 
environments' in the docs (./fabric_lib/README.rst).

Usage:: 

  ./bin/fab <fabric command>:<optional parameter>

"""

from fabric.api import env
from fabric.decorators import task

from fabric_lib.helpers import select_servers, test_connection


try:
    from fabric_lib.tasks import (test, update, deploy, switch)
except ImportError:
    print('To active the fabric_lib submodule run:\n'
          '  git submodule init && git submodule update\n'
          'For more info read https://intranet.gw20e.com/development/plone-projecten/fabric-deployment'
    )
    exit(0)


##############
# Appie config
##############

# CHANGE THE FOLLOWING VARIABLES FOR YOUR BUILDOUT / APPIE ENV:

# Name of the appie environment
appie_env = 'fabric'
# Module which can be updated using git pull
env.modules = ('project.egg', )  
# Local url to Plone
env.site_url = 'http://localhost:{0}/plone_id/'  
# Git uri to buildout
env.buildout_uri = 'git@git.gw20e.com:Project/buildout-name.git'  
# SSH uri's for acc and prd
deploy_info = {
    'acc': {
        'hosts': ['app-{0}-acc@cobain.gw20e.com'.format(appie_env)],
    },
    'prd': {
        'hosts': [
            'app-{0}-prd@192.168.5.52'.format(appie_env), 
            'app-{0}-prd@192.168.5.53'.format(appie_env),
        ],
    },
}


#############
# Env config
#############
env.forward_agent = True
env.always_use_pty = False
env.linewise = True
env.shell = '/bin/dash -e -c'

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
env.buildout_uri = git.Repo().remote().url  # Git uri to buildout

import deployment
env.deploy_info = {
        k:v
        for k, v in deployment.__dict__.items()
        if not k.startswith('_')
        }

try:
   import localfabfile
except ImportError:
    pass

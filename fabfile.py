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

from fabric.api import env, settings
from fabric.decorators import task, hosts


try:
    from fabric_lib.tasks import (test_connection, pull_modules, restart_instances,
        deploy_buildout, switch_buildout, get_master_slave, prepare_release)
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


#############
# Tasks
#############
@task
def check_cluster(layer='acc'):
    cluster = get_master_slave(deploy_info[layer]['hosts'], quiet=False)
    print('\n'.join(
        ['', 'Current cluster info for {0}:'.format(layer)] +
        ["\t{0} is {1}".format(k,v) for k,v in sorted(cluster.items())] +
        ['']))

def select_servers(func):
    def wrapped(layer='acc', server=None, *args, **kwargs):
        servers = deploy_info[layer]['hosts']
        if server:
            matches = [s for s in servers if server in s]
            if matches:
                servers = matches
            else:
                cluster = get_master_slave(servers)
                servers = [cluster[server]]
        for host in servers:
            print host
            with settings(host_string=host):
                func(*args, **kwargs)
    wrapped.__name__ = func.__name__
    wrapped.__doc__ = func.__doc__
    return wrapped

@task
@select_servers
def test():
    """ Test connection """
    test_connection()

@task
@select_servers
def update(tag=None):
    """ Pull modules in env.modules and restart instances """
    pull_modules(tag=tag)
    restart_instances()

@task
@select_servers
def deploy(tag=None):
    """ Create new buildout in release dir """
    deploy_buildout(tag=tag)

@task
@select_servers
def switch(tag=None):
    """ Switch supervisor in current buildout dir to latest buildout """
    switch_buildout(tag=tag)
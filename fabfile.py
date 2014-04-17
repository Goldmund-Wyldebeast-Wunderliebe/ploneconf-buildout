from fabric.api import env, settings
from fabric.decorators import task, hosts

from fabric_lib.tasks import (test_connection, pull_modules, restart_instances, 
    deploy_buildout, switch_buildout, get_master_slave, prepare_release)

# docs in fabric_lib/README.rst

appie_env = 'sbg'
env.modules = ('sbg.theme', )
env.site_url = 'http://localhost:{0}/sbg/'
env.buildout_uri = 'git@git.gw20e.com:sportbedrijf-groningen/buildout-sbg.git'
env.acc_host = 'app-{0}-acc@cobain.gw20e.com'.format(appie_env)
env.prd_hosts = (
    'app-{0}-prd@192.168.5.52'.format(appie_env), 
    'app-{0}-prd@192.168.5.53'.format(appie_env),
)   

#############
# Acceptance
#############
@task
@hosts(env.acc_host)
def acc_test():
    test_connection()

@task
@hosts(env.acc_host)
def acc_update(tag=None):
    pull_modules(tag=tag)
    restart_instances()

@task
@hosts(env.acc_host)
def acc_deploy():
    deploy_buildout(tag='master')

@task
@hosts(env.acc_host)
def acc_switch():
    switch_buildout(tag='master')

#############
# Production
#############
@task
def prd_test():
    get_master_slave()

@task
def prd_deploy(server):
    """ Usage: ./bin/fab prd_deploy:master OR ./bin/fab prd_deploy:slave
    """

    cluster = get_master_slave()

    with settings(host_string=cluster[server]):
        deploy_buildout(tag='master')

@task
def prd_switch(server):
    """ Usage: ./bin/fab prd_deploy:master OR ./bin/fab prd_deploy:slave
    """

    cluster = get_master_slave()

    with settings(host_string=cluster[server]):
        switch_buildout(tag='master')

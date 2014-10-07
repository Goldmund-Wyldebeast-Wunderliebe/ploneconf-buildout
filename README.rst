Buildout
========

rationale (TODO)

How to use this buildout
------------------------
This buildout can be used as a local development buildout and using
fabric remote servers can be controlled to deploy buildouts.


Deployment from local buildout
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Seperated environments
^^^^^^^^^^^^^^^^^^^^^^
Each environment on testing, acceptance or production has it's own user
account. The username of each account contains the name of the environment
 and the name of the env (tst, acc, prd).

For example; if we have an environment with the name example, three system
users are needed: app-example-tst, app-example-acc and app-example-prd.

A Puppet module called `puppet-appie`_ can be used to automate the setup of
the accounts.

.. _`puppet-appie`: https://github.com/Goldmund-Wyldebeast-Wunderliebe/puppet-appie

Getting started
---------------

Initial setup
~~~~~~~~~~~~~
First checkout the library/module which contains the fabric functionality::

    git submodule init
    git submodule update

After the submodule is cloned there should be a ``fabric_lib`` directory with
several files.

Create a virtual environment, bootstrap the buildout used for development
and run buildout::

    virtualenv .
    python bootstrap.py -c buildout-dvl.cfg
    ./bin/buildout -c buildout-dvl.cfg

Start the zeo server and run the instance in the foreground::

    ./bin/zeo start
    ./bin/instance fg

Configuring remote deployment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The configure remote deployment a server with SSH access is needed. In this
example we will deploy a Plone buildout to a cluster.

In ``deployment.py`` the config for the remote is stored. The following
attributes are used, change the attributes to your needs.

``_base_port``
    This number is used to define port numbers for Plone, ZODB server, Varnish
    caching proxy and the HAProxy load balancer.

``_env_name``
    The name of your enviroment, this can be the name of a customer or the
    name of the Plone site. The environment name is used in the user account,
    make sure only lower case is used and avoid white spaces.

``_site_id``
    This is the id of the Plone site. It is used in the config for the webserver.

``_flying_ip``
    The flying IP address of a cluster, omit this one if no cluster setup is used.

``_servers``
    Configure one ore more servers which are used for remote deployment. Each
    server has a name and a IP address or a domain name.

``_modules``
    Python eggs or Plone modules which are in own maintenance #TODO improve

``_third_party_modules``
    List third party modules which are used from source #TODO improve

``default``
    Sets the default enviroment, this is tst (test environment) by default.

Deploy to remote servers
~~~~~~~~~~~~~~~~~~~~~~~~

Prerequisites:

 * The attributes in ``deployment.py`` are changed to your the needs of your environment
 * At least one user account with SSH access on the remote server(s), ie. app-example-prd
 * Fabric to deploy, it is included in this buildout in the bin directory

Optional:

 * Configure `SSH Agent Forwarding`_, forwarding can be used if you have private
   repositories. It allows you to use your local SSH keys.

First test if we have a SSH connection to the test environment on the server using::

    ./bin/fab test:layer=tst

The layer parameter can be omitted because the test environment is the default::

    ./bin/fab test

Each server should return an output similar to the one below::

    # ./bin/fab test
    app-example-tst@192.168.3.45
    Testing example tst connection for app-example-tst@192.168.3.45
    [app-fabric-tst@192.168.3.45] run: hostname ; whoami ; pwd
    [app-fabric-tst@192.168.3.45] out: patia
    [app-fabric-tst@192.168.3.45] out: app-example-tst
    [app-fabric-tst@192.168.3.45] out: /opt/APPS/example/tst

To deploy a buildout run the following command. A deployment will run buildout on
the server(s) defined in the ``_servers`` deployment attribute.

    ./bin/fab deploy

Further reading is in the fabric buildout library `fabric_lib`_.

.. _`SSH Agent Forwarding`: https://developer.github.com/guides/using-ssh-agent-forwarding/
.. _`fabric_lib`: http://TODO/

Further usage
-------------

Migrating from existing buildout templates with DTAP-config. TODO

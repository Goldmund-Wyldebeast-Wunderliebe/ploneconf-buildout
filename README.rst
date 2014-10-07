Buildout
========

rationale

How to use this buildout
------------------------
This buildout can be used as a local development buildout and using
fabric remote servers can be controlled to deploy buildouts.

Appie concept
-------------

Initial setup
-------------
First checkout the library/module which contains the fabric functionality::

    git submodule init
    git submodule update

After the submodule is cloned there should be a ``fabric_lib`` directory with
several files.

Create a virtual environment, bootstrap the buildout used for development
and run buildout::

    virtualenv-2.7 .
    python bootstrap.py -c buildout-dvl.cfg
    ./bin/buildout -c buildout-dvl.cfg

 Start the zeo server and run the instance in the foreground::

    ./bin/zeo start
    ./bin/instance fg

Configuring remote deployment
-----------------------------

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


Deploy to remote servers
------------------------



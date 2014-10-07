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
attributes are used:

``_base_port``
    This number is used to define port numbers for Plone, ZODB server, Varnish
    caching proxy and the HAProxy load balancer.

``_env_name``
    The name of your enviroment, this can be the name of a customer or the
    name of the Plone site. The environment name is used in the user account,
    make sure only lower case is used and avoid white spaces.

``_site_id``
    This is the id of the Plone site. It is



Deploy to remote servers
------------------------



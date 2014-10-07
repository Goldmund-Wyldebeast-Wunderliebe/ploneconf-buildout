Buildout
========

rationale

How to use this buildout
------------------------
This buildout can be used as a local developement buildout and using
fabric remote servers can be controlled to deploy buildouts.

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


Deploy to remote servers
------------------------



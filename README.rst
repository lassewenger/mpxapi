MPX API Library
===============

Simple, low-level handling of the MPX API with built-in authentication functions. Handles authentication, and
automatically supplies tokens on called commands.
Also automatically fetches the service registry to use for calling commands.

Notice to updaters
------------------
Starting in version 0.1.0, httpError is by default on, which should make status codes usable.

Usage
-----

To get started, supply your credentials: username, password, account id (This is
a URL and can be found on the "About" screen in the MPX console).

.. code-block:: python

    import mpxapi
    api = MPXApi(username=username, password=password, account=account, tld="eu")

    params= {"schema": "2.15.0", "searchSchema": "1.3.0", "range": "-1", "pretty": "true"}
    req = api.command(service="Entertainment Data Service", path="/data/Program", method="GET", params=params)


Another option is to use premade models for some of the data services

.. code-block:: python

    from mpxapi import MPXApi
    from mpxapi.entertainment import Programs

    api = MPXApi(username=username, password=password, account=account, tld="eu")
    programs = Programs(api=api)

    programs.get({"range"; "-1"})


To sign out after using the API (thereby invalidating the token)

.. code-block:: python

    api.sign_out()

This will invalidate the authentication token, and require a new call to api.sign_in()

Installation
------------

.. code-block:: bash

    pip install mpxapi

It can also be added to requirements.txt as is.

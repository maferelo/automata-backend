Automata's python backend 
=========================

.. toctree::
   :hidden:
   :maxdepth: 1

   license
   reference

The command-line interface prints random facts to your console,
using the `Wikipedia API <https://en.wikipedia.org/api/rest_v1/#/>`_.


Installation
------------

To install the project,
run this command in your terminal:

.. code-block:: console

   $ pip install app


Usage
-----

Project's usage looks like:

.. code-block:: console

   $ app [OPTIONS]

.. option:: -l <language>, --language <language>

   The Wikipedia language edition,
   as identified by its subdomain on
   `wikipedia.org <https://www.wikipedia.org/>`_.
   By default, the English Wikipedia is selected.

.. option:: --version

   Display the version and exit.

.. option:: --help

   Display a short usage message and exit.

.. image:: https://img.shields.io/pypi/v/shortbus.svg
        :target: https://pypi.python.org/pypi/shortbus

.. image:: https://img.shields.io/travis/brmc/shortbus.svg
        :target: https://travis-ci.org/brmc/shortbus

.. image:: https://readthedocs.org/projects/shortbus/badge/?version=latest
        :target: https://shortbus.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/brmc/shortbus/shield.svg
     :target: https://pyup.io/repos/github/brmc/shortbus/
     :alt: Updates

========
shortbus
========

Tools to convert Sublime Text snippets into Jetbrains live templates and vice versa


* Free software: MIT license
* Documentation: something is wrong with the read-the-docs build, so for those in a *nix environment, to view the documentation do this:

.. code-block:: console

    $ git clone https://github.com/brmc/shortbus
    $ cd shortbus
    $ make docs

a browser should open with the docs

Requirements:
-------------

- python3.6+
- lxml
- pyyaml

Quick Start
-----------

Install library:

.. code-block:: console

    $ pip install shortbus

Do stuff:

.. code-block:: python

    transpilers.import_from_yml('./my.yml')
        .import_from_sublimetext('~/path/to/sublimetext/snippetdir/)
        .import_from_jetbrains('~/.PyCharm2016.3/config/liveTemplates/Djaneiro.xml')
        .export_to_jetbrains('shortbus.xml')
        .export_to_yml('shortbus.yml')

.. include:: ./docs/ymlsyntax.rst


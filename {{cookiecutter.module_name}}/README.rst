{{cookiecutter.module_display_name}}
=============

.. image:: https://img.shields.io/travis/{{cookiecutter.github_name}}/{{cookiecutter.github_repo}}/master.svg
    :target: https://travis-ci.org/{{cookiecutter.github_name}}/{{cookiecutter.github_repo}}
    :alt: Linux and MacOS Build Status
.. image:: https://readthedocs.org/projects/{{cookiecutter.module_name}}/badge/?version=latest
    :target: http://{{cookiecutter.module_name}}.readthedocs.io
    :alt: Documentation Build Status
.. image:: https://img.shields.io/codecov/c/github/{{cookiecutter.github_name}}/{{cookiecutter.github_repo}}/master.svg
    :target: https://codecov.io/gh/{{cookiecutter.github_name}}/{{cookiecutter.github_repo}}
    :alt: Test Suite Coverage
.. image:: https://img.shields.io/pypi/v/{{cookiecutter.module_name}}.svg
    :target: https://pypi.python.org/pypi/{{cookiecutter.module_name}}
    :alt: PyPI Version

{{cookiecutter.module_description}}

Install
-------

{{cookiecutter.module_display_name}} is available on PyPI can be installed with `pip <https://pip.pypa.io>`_.::

    $ pip install {{cookiecutter.module_name}}

To install the latest development version from `GitHub <https://github.com/{{cookiecutter.github_repo}}>`_::

    $ pip install git+git://github.com/{{cookiecutter.github_repo}}.git

Usage
-----

After installing {{cookiecutter.module_display_name}} you can use it like any other Python module.
Here's a very simple example:

.. code-block:: python

    import {{cookiecutter.module_name}}
    # Fill this section in with the common use-case.

::

    {{cookiecutter.module_name}}

To see the full list of options:

::

    {{cookiecutter.module_name}} --help
    
    Options:
      debug:            drop a debugger if an exception is raised
      help (-h):        argparse help
      log-level (-l)    logging level (default=INFO)

API Reference
-------------

The `API Reference on readthedocs.io <http://{{cookiecutter.module_name}}.readthedocs.io>`_ provides API-level documentation.

Support / Report Issues
-----------------------

All support requests and issue reports should be
`filed on GitHub as an issue <https://github.com/{{cookiecutter.github_name}}/{{cookiecutter.github_repo}}/issues>`_.

Releasing
---------

::

    git checkout master
    git tag -a vX.Y.Z
    git push origin --tags

Test
----

Running unit tests::

    make test

Running linter::

    make lint

Running tox::

    make test-all

License
-------

{{cookiecutter.license}}

ksindi's Cookiecutter PyPackage
===============================

Repo to create new python packages from cookiecutter

Usage
-----

Change to the directory you want your project to be in::

    $ cd ~/git

Install the `cookiecutter <https://github.com/audreyr/cookiecutter>`_ module via pip::

    $ pip install cookiecutter
    
Then run cookiecutter to get the latest version of the template.
It'll ask you a few questions like your Github user name, repo name, etc::

    $ cookiecutter gh:ksindi/cookiecutter-pypackage

Be sure to change the licenses everywhere if you're using something besides MIT.

The files you should change if you're using a non-MIT license are:

* `LICENSE`

Do a quick look at all ``.rst`` files to make sure the number of underlines is correct for titles. :)

After this commit, you should sign up for the following services and set their permissions on Github:

* `Travis CI <https://travis-ci.org/>`_
* `Codecov <https://codecov.io/gh>`_
* `Readthedocs <https://readthedocs.org/>`_

License
-------
CC0-1.0.

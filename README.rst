ksindi's Cookiecutter PyPackage
===============================

Repo to create a new python package using cookiecutter.

Usage
-----

Change to the directory you want your project to be in::

    cd ~/git

Install the `cookiecutter <https://github.com/audreyr/cookiecutter>`_ module via pip::

    pip install cookiecutter
    
Then run cookiecutter to get the latest version of the template.
It will ask you a few questions like your GitHub user name, repo name, etc::

    cookiecutter gh:ksindi/cookiecutter-pypackage

Be sure to change the licenses everywhere if you're using something besides MIT.

The files you should change if you're using a non-MIT license are:

* `LICENSE`

Do a quick look at all ``.rst`` files to make sure the number of underlines is correct for titles.

Set up a GitHub repo {{cookiecutter.github_repo}} without an initial commit and commit/push the directory::

    cd ~/git/{{cookiecutter.module_name}}/
    git init
    git add .
    git commit -m "Initial commit"
    git remote add origin https://github.com/{{cookiecutter.github_repo}}.git
    git push origin master

After this commit, you should sign up for the following services and set their permissions on GitHub:

* `Travis CI <https://travis-ci.org/>`_
* `Codecov <https://codecov.io/gh>`_
* `Readthedocs <https://readthedocs.org/>`_

License
-------
CC0-1.0.

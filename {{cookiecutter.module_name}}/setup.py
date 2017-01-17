# -*- coding: utf-8 -*-
"""Distutils setup file, used to install or test '{{cookiecutter.module_name}}'."""
from __future__ import print_function

import textwrap
from setuptools import setup

with open('README.rst') as f:
    readme = f.read()

if __name__ == '__main__':
    setup(
        name='{{cookiecutter.module_name}}',
        description='{{cookiecutter.module_description}}',
        long_description=readme,
        url='http://{{cookiecutter.module_name}}.readthedocs.io',
        use_scm_version=True,
        author='{{cookiecutter.full_name}}',
        author_email='{{cookiecutter.email}}',
        maintainer='{{cookiecutter.full_name}}',
        maintainer_email='{{cookiecutter.email}}',
        install_requires=[
            'setuptools_scm>=1.15.0',
        ],
        setup_requires=[
            'setuptools>=18.0',
            'pytest-runner',
            'setuptools_scm>=1.15.0',
            'sphinx_rtd_theme',
        ],
        tests_require=[
            'pytest',
            'pytest-flake8',
        ],
        extras_require={
            ':python_version=="2.7"': ['mock'],
        },
        zip_safe=False,
        include_package_data=True,
        classifiers=textwrap.dedent("""
            Development Status :: 4 - Beta
            Intended Audience :: Science/Research
            License :: OSI Approved :: {{cookiecutter.license}}
            Natural Language :: English
            Environment :: Console
            Programming Language :: Python :: 2
            Programming Language :: Python :: 2.7
            Programming Language :: Python :: 3
            Programming Language :: Python :: 3.4
            Programming Language :: Python :: 3.5
            Programming Language :: Python :: 3.6
            Topic :: Scientific/Engineering
            """).strip().splitlines(),
        keywords=['{{cookiecutter.module_name}}'],
        license='{{cookiecutter.license}}',
        entry_points={
            'console_scripts': [
                '{{cookiecutter.module_name}} = {{cookiecutter.module_name}}.__main__:main'
            ]
        },
    )

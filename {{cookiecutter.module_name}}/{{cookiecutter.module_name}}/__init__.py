# -*- coding: utf-8 -*-
# flake8: noqa
"""{{cookiecutter.module_name}} library.

:copyright: (c) 2017 by {{cookiecutter.full_name}}.
:license: MIT, see LICENSE for more details.
"""
import logging

from setuptools_scm import get_version

__title__ = '{{cookiecutter.module_name}}'
__author__ = '{{cookiecutter.full_name}}'
__license__ = 'MIT'
__email__ = '{{cookiecutter.email}}'
# __version__ = get_version(root='..', relative_to=__file__)


# Set default logging handler to avoid "No handler found" warnings.
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())

__all__ = []

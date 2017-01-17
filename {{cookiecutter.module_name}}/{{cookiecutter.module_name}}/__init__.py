# -*- coding: utf-8 -*-
# flake8: noqa
"""{{cookiecutter.module_name}} library.

:copyright: (c) {{year}} by {{cookiecutter.full_name}}.
:license: {{license}}, see LICENSE for more details.
"""
import logging

from pkg_resources import get_distribution, DistributionNotFound

__title__ = '{{cookiecutter.module_name}}'
__author__ = '{{cookiecutter.full_name}}'
__license__ = 'MIT'
__email__ = '{{cookiecutter.email}}'
try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass

# Set default logging handler to avoid "No handler found" warnings.
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())

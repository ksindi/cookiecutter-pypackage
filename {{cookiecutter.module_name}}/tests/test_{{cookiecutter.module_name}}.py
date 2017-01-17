# -*- coding: utf-8 -*-
"""pytest unittests"""
import os
import shlex

try:
    from unittest import mock
except ImportError:
    import mock

from {{cookiecutter.module_name}} import __main__

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def test_parser():
    parser = __main__.create_parser()
    cmd_args_str = ""
    args = parser.parse_args(shlex.split(cmd_args_str))
    
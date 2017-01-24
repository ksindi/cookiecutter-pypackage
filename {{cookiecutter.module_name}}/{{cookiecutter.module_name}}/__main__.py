#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""{{cookiecutter.module_name}} CLI.

Options:
  debug:            drop a debugger if an exception is raised
  help (-h):        argparse help
  log-level (-l)    logging level (default=INFO)

Usage:
  {{cookiecutter.module_name}}
"""
import sys
import os.path
import logging
from argparse import RawDescriptionHelpFormatter, ArgumentParser

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

logger = logging.getLogger(__name__)
LOGFORMAT = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'


def debug_hook(type_, value, tb):
    # http://stackoverflow.com/a/1237407/690430
    if hasattr(sys, 'ps1') or not sys.stderr.isatty():
        sys.__excepthook__(type_, value, tb)
    else:
        import traceback
        import pdb
        traceback.print_exception(type_, value, tb)
        print(u"\n")
        pdb.pm()


def create_parser():
    parser = ArgumentParser(description=__doc__,
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('--log-level', '-l', type=str.upper, default='INFO')
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    print("Args: ", args)

    if args.debug:
        sys.excepthook = debug_hook

    numeric_level = getattr(logging, args.log_level, None)
    logging.basicConfig(format=LOGFORMAT)
    logger.setLevel(numeric_level)

    return {{cookiecutter.module_name}}(**vars(args))


def {{cookiecutter.module_name}}(**kwargs):
    pass

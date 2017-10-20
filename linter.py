#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Ahmad Samiei
# Copyright (c) 2017 Ahmad Samiei
#
# License: MIT
#

"""This module exports the Psalm plugin class."""

from SublimeLinter.lint import Linter


class Psalm(Linter):
    """Provides an interface to psalm."""

    syntax = ('php', 'html', 'html 5')
    tempfile_suffix = '.php'
    cmd = ('psalm', '*', '@')
    defaults = {
        '@monochrome': '-m',
        '@root': '--root=${project}',
        '@config': '--config=${project}/psalm.xml'
    }
    regex = r'^.*:(?P<line>\d+):(?P<col>\d+) - (?P<message>.+)$'

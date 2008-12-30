#!/usr/bin/env python

import os.path
from setuptools import setup

setup(
    name = 'TracInlineMacro',
    packages = ['inline'],
    version = '0.11.0',

    author = 'Douglas Clifton',
    author_email = 'dwclifton@gmail.com',
    description = 'Returns raw, inline XHTML markup that has been validated and sanitized.', 
    long_description = open(os.path.join(os.path.dirname(__file__), 'README')).read(),
    keywords = '0.11 dwclifton macro wiki',
    url = 'http://trac-hacks.org/wiki/InlineMacro',
    license = 'BSD',

    entry_points = { 'trac.plugins': [ 'inline.macro = inline.macro' ] },
    classifiers = ['Framework :: Trac'],
    install_requires = ['Trac'],
)

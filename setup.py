#!/usr/bin/env python
'''
Installer script for pthbetter.
'''

from setuptools import setup

import re
VERSIONFILE="_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(
    name = "pthbetter",
    description = "WhatBetter's fork - Greetz Zach Denton",
    author = 'PTH',
    author_email = 'pth@pth.com',
    version = verstr,
    url = 'https://github.com/aktavor69/pthbetter',
    py_modules = [
        '_version',
        'tagging',
        'transcode',
        'pthapi'
    ],
    scripts = ['pthbetter'],
    install_requires = [
        'mutagen',
        'mechanize',
        'requests'
    ]
)

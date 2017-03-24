'''
Installer script for nwbetter.
'''

from setuptools import setup

import re
VERSIONFILE = "_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(
    name="nwbetter",
    description="WhatBetter's fork - Greetz Zach Denton",
    author='NW',
    author_email='nw@nw.com',
    version=verstr,
    url='https://github.com/aktavor69/nwbetter',
    py_modules=[
        '_version',
        'tagging',
        'transcode',
        'nwapi'
    ],
    scripts=['nwbetter'],
    install_requires=[
        'mutagen',
        'mechanize',
        'requests'
    ]
)

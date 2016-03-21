#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
  name = 'pyviscam',
  packages = ['pyviscam'], 
  version = '0.0.1',
  description = 'Control camera through Visca protocol',
  author = 'Pixel Stereo',
  url='https://github.com/PixelStereo/PyVisca', 
  download_url = 'https://github.com/PixelStereo/PyVisca/tarball/0.0.1', 
  classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
    'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# SITEURL = 'http://yichuans.github.io/human-footprint/output'
SITEURL = 'http://world-heritage-analyses.iucn.org/human-footprint'
SEARCH_URL = SITEURL + '/search'
OUTPUT_PATH = 'output_wha/'

MENUITEMS = [('country', SITEURL + '/tags')]

RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing
DISQUS_SITENAME = 'human-footprint-natural-world-heritage'
GOOGLE_ANALYTICS = 'UA-61833965-5'
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'IUCN and WCS'
SITENAME = u'Human Footprint and Forest Loss in natural World Heritage sites'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# # Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# additional
HIDE_SIDEBAR = True

JINJA_EXTENSIONS = ['jinja2.ext.i18n']
THEME = r"./pelican-bootstrap3"

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['i18n_subsites']

LOAD_CONTENT_CACHE = False

DISQUS_SITENAME = 'hffl'
CC_LICENSE = 'CC-BY'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

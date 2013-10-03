#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

AUTHOR = u'Filipe Fernandes'
SITENAME = u'python4oceanographers'
SITESUBTITLE = u'Learn python with examples applied to marine sciences.'
# Change in publishconf.py and ignore the WARNING.
SITEURL = ''

# Times and dates.
DEFAULT_DATE_FORMAT = '%b %d, %Y'
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = u'en'

# Set the article URL.
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Title menu options.
MENUITEMS = [('Archives', '/archives.html'),
             ('Home Page', 'http://ocefpaf.tiddlyspot.com/')]
NEWEST_FIRST_ARCHIVES = False

# Github include settings.
GITHUB_USER = 'ocefpaf'
GITHUB_REPO_COUNT = 5
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

# Blogroll.
LINKS =  (('PyAOS', 'http://pyaos.johnny-lin.com/'),
          ('drclimate', 'http://drclimate.wordpress.com/'),
          ('Software Carpentry',
           'http://software-carpentry.org/blog/index.html'),)

# Social widget.
#SOCIAL = (('You can add links in your config file', '#'),
          #('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# STATIC_OUT_DIR requires pelican 3.3.
STATIC_OUT_DIR = ''
STATIC_PATHS = ['images', 'figures', 'downloads']
FILES_TO_COPY = [('favicon.png', 'favicon.png')]
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

# Theme and plug-ins.
# http://github.com/duilio/pelican-octopress-theme/
# http://github.com/getpelican/pelican-plugins/ (original)
# https://github.com/jakevdp/pelican-plugins.git (liquid_tags branch)
path = '/home/filipe/Dropbox/Blog/blog-virtual-env'
THEME = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                     'octopress-theme')
PLUGIN_PATH = '%s/pelican-plugins' % path
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal']

# The theme file should be updated so that the base header contains the line:
# {% if EXTRA_HEADER %}
# {{ EXTRA_HEADER }}
# {% endif %}

# This header file is automatically generated by the notebook plugin.
EXTRA_HEADER = open('_nb_header_mod.html').read().decode('utf-8')

# Sharing
TWITTER_USER = 'ocefpaf'
GOOGLE_PLUS_USER = '116220614704100857098'
GOOGLE_PLUS_ONE = True
GOOGLE_PLUS_HIDDEN = False
FACEBOOK_LIKE = True
TWITTER_TWEET_BUTTON = True
TWITTER_LATEST_TWEETS = True
TWITTER_FOLLOW_BUTTON = True
TWITTER_TWEET_COUNT = 3
TWITTER_SHOW_REPLIES = 'false'
TWITTER_SHOW_FOLLOWER_COUNT = 'true'

# RSS/Atom feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = 'atom.xml'

# Search
SEARCH_BOX = True

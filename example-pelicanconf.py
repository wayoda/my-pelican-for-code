#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'NameOfAuthor'
COPYRIGHT = u'&copy; Year-Year'
SITE_NAME = u'TheSiteName'
SITEURL = u''
SITE_DESCRIPTION = u'WhatIsThisAbout'
PROJECT_NAME = u'ProjectName'
PROJECT_URL = u'Projct-URL'
PROJECT_MAIL = u'MailAddress'

#All the content is in content
PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

#This links to our theme 
THEME = "./themes/wayoda-github"

#We want syntax-highlighting
MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra']

# We want document-relative URLs 
RELATIVE_URLS = True

PATH=u''
#Here are our static markdown pages 
PAGE_PATHS = [u'pages']
#We might want to refer to some images too
STATIC_PATHS = ['images']

#Appeears in  the footer
VERSION = u'1.0.0'

#Not a Blog we don't need these
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#Syntax as on github
SYNTAX_THEME=u'github'

#If you want pages to show up in the Menu on top 
#add them here. (If empty we have no Menu on top)

MENU = [(u'Home','index.html'),
        (u'Hardware',u'pages/hardware.html'),
        (u'Software',u'pages/software.html'),
        (u'FAQ',u'pages/faq.html'),
        ]


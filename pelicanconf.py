#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'David García Garzón'
SITENAME = 'Desconexión IBEX35'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
	('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
    ('You can modify those links in your config file', '#'),
)

MENUITEMS=(
	('Proyecto', 'pages/el-proyecto.html'),
	('Simulador', 'pages/revote-simulador-online-de-flujos-electorales.html'),
	('Fundamentos', 'category/fundamentos.html'),
	#('Mitos', 'mitos.md'),
	#('Memes', 'memes.md'),
)
# Social widget
SOCIAL = (
	('Facebook', 'https://www.facebook.com/DesconexionIBEX35'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

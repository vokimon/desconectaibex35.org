#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'David García Garzón'
SITENAME = 'Desconecta del IBEX35'
SITESUBTITLE = '¿Porqué seguir alimentando a la bestia?'
SITEURL = ''
SITESUMMARY='Resumen mu corto'
#GITHUB_URL = 'http://github.com/vokimon/desconectaibex35.org'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'es'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M'
DEFAULT_METADATA = {
	'status': 'draft',
}

ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feed.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS_WIDGET_NAME="Páginas Similares"
LINKS = (
	('Pam a Pam', 'https://pamapam.org'),
	('Opcions', 'https://opcions.coop'),
	('XES', 'https://xes.cat'),
)

PLUGINS=[
	'pelican.plugins.more_categories',
	'pelican_youtube',
]

MENUITEMS=(
	('Proyecto', 'pages/la-idea.html'),
	('Simulador', 'pages/revote-simulador-online-de-flujos-electorales.html'),
	('Fundamentos', 'category/fundamentos.html'),
)
# Social widget
SOCIAL = (
	('DesconexionIBEX35', 'https://www.facebook.com/DesconexionIBEX35'),
)

DEFAULT_PAGINATION = 10

DISPLAY_CATEGORIES_ON_MENU=True
DISPLAY_PAGES_ON_MENU=True
SUMMARY_USE_FIRST_PARAGRAPH = True
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
        },
        'markdown.extensions.admonition': {},
        'markdown.extensions.toc': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.tables': {},
    },
    'output_format': 'html5',
}

THEME='themes/notmyidea'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

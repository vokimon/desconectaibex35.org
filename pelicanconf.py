#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

def categories(ctx, *topics):
	#print(ctx.metadata)
	ctx.parser.parseChunk(ctx.parent, ''.join([
		"""::: topicicons width="64" heigth="auto" style="float:right; margin-left:3ex; text-align: center; background: white"\n""",
		] + [
	"""    [![{Topic}]({{static}}/images/categories/{topic}.png "{Topic}")]"""
	"""({{category}}/{Topic})<br>{Topic}\n\n\n""".format(
			topic = category.lower(),
			Topic = category.title(),
		)
		for category in topics or ctx.metadata.get('category')[0].split(', ')
	]))


AUTHOR = 'David García Garzón'
SITENAME = 'Desconecta del IBEX35'
SITESUBTITLE = '¿Vas a seguir alimentando a la bestia?'
SITEURL = ''

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'es'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_METADATA = {
	'status': 'draft',
}

PATH = 'content'
DIRECT_TEMPLATES = ['index', 'archives', 'tags', 'categories', 'search', '404']
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
STATIC_URL = '{path}'
STATIC_SAVE_AS = '{path}'
STATIC_PATHS=[
	'images',
	'extra',
	'blog',
	'files',
]
EXTRA_PATH_METADATA = {
    'extra': {'path': ''},
}

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

MENUITEMS=(
	('Proyecto', '/pages/la-idea.html'),
)
# Social widget
#SOCIAL_PROFILE_LABEL="En contacto"
SOCIAL = (
	('GitHub', 'http://github.com/vokimon/desconectaibex35.org'),
	('DesconexionIBEX35', 'https://www.facebook.com/DesconexionIBEX35'),
)

DEFAULT_PAGINATION = 20

DISPLAY_CATEGORIES_ON_MENU=False
DISPLAY_PAGES_ON_MENU=False
SUMMARY_USE_FIRST_PARAGRAPH = True

PLUGIN_PATHS=[
	'./pelican-plugins',
]
PLUGINS=[
	'pelican_javascript',
	'pelican.plugins.more_categories', # Multiple categories per article, hierarchical categories
	'video_privacy_enhancer', # (Unused) Embed videos with privacy until played
	'neighbors', # To show next-prev links in articles
	'extract_toc', # Aside responsive TOC
	'tipue_search', # Search
	'deadlinks', # complaint on deadlinks and provide archive.org versions
	#'assets', # join and minimize css and js
]

MARKDOWN = {
	'extension_configs': {
		'markdown.extensions.codehilite': {
			'css_class': 'highlight',
		},
        'markdown.extensions.admonition': {},
        'markdown.extensions.toc': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.tables': {},
		'markdown.extensions.attr_list': {},
		'customblocks': {
			'generators': {
				'categories': categories,
			},
		}
    },
    'output_format': 'html5',
}

THEME='elegant'

# ELEGANT THEME CUSTUMIZATION
THEME_STATIC_DIR = 'theme/'
THEME_TEMPLATES_OVERRIDES = [
	'templates',
]
SEARCH_BOX = False
LANDING_PAGE_TITLE = "Desconecta del IBEX-35"

FEATURED_IMAGE = 'desconexionibex35-logo.png'
SITE_DESCRIPTION="""\
**No queremos apoyar con nuestro dinero**
a las grandes empresas (del IBEX-35 y otras)
por los diversos abusos que cometen.

**Investigamos, generamos y fomentamos alternativas**
con diferentes niveles de compromiso
que se puedan adaptar a las posibilidades de cada persona.
Las promovemos y **nos acompañamos en el salto**.

Si encuentras este proyecto interesante, no lo dudes, **¡súmate!**
"""

import datetime
SITE_UPDATED = datetime.date.today()

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

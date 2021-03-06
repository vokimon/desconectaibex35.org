#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys
sys.path.append(os.curdir)
import generators

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
DIRECT_TEMPLATES = ['index', 'archives', 'tags', 'categories', 'search']
THEME_TEMPLATES_OVERRIDES = ['templates']
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
	'uploads',
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
	('Proyecto', (
        ('Motivación', 'la-idea/'),
        ('Estrategia', 'estrategias/'),
        ('Colabora', 'colabora/'),
    )),
    ('Sectores', "#section_sectors"),
    ('Noticias', "#section_news"),
	('Información', (
        ("Alternativas", 'lista-de-alternativas'),
        ("Telecos: Guifi.net", 'telecos-guifi-net'),
        ("Electricas: Som energia", 'electricas-som-energia'),
#        ("Quienes somos", ''),
#        ("Recursos", ''),
#        ("Créditos", ''),
    )),
)
VOKIBLOG_SITELOGO = 'images/desconexionibex35-logo-black.png'
VOKIBLOG_BANNER = "images/logo-desconexionibex35.svg"
VOKIBLOG_HIGHLIGHTS = (
    dict(
        title = "Desconecta",
        subtitle = "Deja de alimentar a la bestia",
        description  = 
            "El IBEX y las grandes empresas perjudican "
            "a la ciudadania, a la economía y al medioambiente. "
            "Por eso, queremos dejar de nutrirles con nuestro dinero.",
        action = "Los motivos",
        action_url = "/la-idea/",
        action_class = "is-info",
    ),
    dict(
        title = "Campaña",
        subtitle = "Qué hacemos",
        description  = 
            "Buscamos alternativas a las grandes empresas. "
            "Las difundimos y las facilitamos, acompañandonos en el tránsito. "
            "Si no existen, fomentamos su creación.",
        action = "Como",
        action_url = "/estrategias/",
        action_class = "is-success",
    ),
    dict(
        title = "Alternativas",
        subtitle = "Por sectores",
        description =
            "De cada sector presentamos varias alternativas "
            "para que cada persona encuentre la vía de desconexión que más le funcione, "
            "explicando sus bondades y inconvenientes.",
        action = "Descúbrelas",
        action_url = "",
        action_class = "is-danger",
    ),
)
VOKIBLOG_SOCIAL = (
#	('eMail', '', 'has-text-light-grey', "fas fa-envelope"),
	('Feed RSS', FEED_ALL_ATOM, 'has-text-danger', 'fas fa-rss'),
#	('Mastodon', '', 'has-text-primary','fab fa-mastodon'),
	('Facebook', 'https://www.facebook.com/DesconexionIBEX35', 'has-text-link', 'fab fa-facebook'),
#	('Twitter', '', 'has-text-primary','fab fa-twitter'),
	('GitHub', 'http://github.com/vokimon/desconectaibex35.org', 'has-text-dark', 'fab fa-github'),
)

# Social widget
#SOCIAL_PROFILE_LABEL="En contacto"
SOCIAL = (
	('GitHub', 'http://github.com/vokimon/desconectaibex35.org'),
	('DesconexionIBEX35', 'https://www.facebook.com/DesconexionIBEX35'),
)
SHARE_POST_INTRO = "Compártelo"
VOKI_SHARE_LINKS = (
	('facebook', 'Facebook', 'has-text-link', 'fab fa-facebook'),
    ('twitter', 'Twitter', 'has-text-primary', 'fab fa-twitter'),
    ('mastodon', 'Mastodon', 'has-text-link-dark', 'fab fa-mastodon'),
    ('telegram', 'Telegram', 'has-text-primary', 'fab fa-telegram'),
    ('linkedin', 'Linkedin', 'has-text-link', 'fab fa-linkedin'),
    ('whatsapp', 'WhatsApp', 'has-text-success-dark', 'fab fa-whatsapp'),
)


DEFAULT_PAGINATION = 20

DISPLAY_CATEGORIES_ON_MENU=False
DISPLAY_PAGES_ON_MENU=False
SUMMARY_USE_FIRST_PARAGRAPH = True

PLUGIN_PATHS=[
	'./pelican-plugins',
]
PLUGINS=[
    'summary', # Choose the article summary
    'representative_image', # extract images from summary and pick one as featured image
	'pelican_javascript',
	'pelican.plugins.more_categories', # Multiple categories per article, hierarchical categories
	#'video_privacy_enhancer', # (Unused) Embed videos with privacy until played
	'neighbors', # To show next-prev links in articles
	'extract_toc', # Aside responsive TOC
	'tipue_search', # Search
	'deadlinks', # complaint on deadlinks and provide archive.org versions
	'pelican-yaml-metadata', # full yaml markdown metadata (https://github.com/pR0Ps/pelican-yaml-metadata)
	#'assets', # join and minimize css and js
    'share_post', # Share post in social media
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
                'categories': generators.categories,
                'rtve': generators.rtve,
            },
            'config': {
                'youtube_inlineFluidStyle': True,
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
No queremos apoyar con nuestro dinero
a las grandes empresas
por los diversos abusos que cometen.

Investigamos, creamos y fomentamos alternativas,
y nos acompañamos en el salto.

Si encuentras este proyecto interesante, no lo dudes, ¡súmate!
"""

import datetime
SITE_UPDATED = datetime.date.today()

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# vim et ts=4 sw=4

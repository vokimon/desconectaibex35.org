#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import requests
from yamlns import namespace as ns
import html


def categories(ctx, *topics):
    #print(ctx.metadata)
    ctx.parser.parseChunk(ctx.parent, ''.join([
        """::: category-list width="64" heigth="auto" style="float:right; margin-left:3ex; text-align: center; background: white"\n""",
        ] + [
    """    [![{Topic}]({{static}}/images/categories/{topic}.png "{Topic}")]"""
    """({{category}}/{Topic})<br>{Topic}\n\n\n""".format(
            topic = category.lower(),
            Topic = category.title(),
        )
        for category in topics or ctx.metadata.get('category')[0].split(', ')
    ]))

def categories(ctx, *topics):
	return

def rtve(id, title=''):
    thumb='https://img2.rtve.es/css/rtve.commons/rtve.header.footer/i/logoRTVEes.png'
    link=f'https://www.rtve.es/v/{id}/'
    embeded = f"https://secure-embed.rtve.es/drmn/embed/video/{id}/"
    response=requests.get(f'http://api.rtve.es/api/videos/{id}.json',
        headers={'Cache-Control': 'no-cache'})
    if response.ok:
        metadata = ns.loads(response.text)
        thumb = metadata.page['items'][0].thumbnail
        title = html.escape(metadata.page['items'][0].longTitle)
        link = html.escape(metadata.page['items'][0].htmlUrl)
    return f"""\
<div
    style="width:100%;padding-top:64%;position:relative;border-bottom:1px solid #aaa;display:inline-block;background:#eee;background:rgba(255,255,255,0.9);"
>
    <iframe
        src="{embeded}"
        name="{title}"
        style="width:100%;height:90%;position:absolute;left:0;top:0;overflow:hidden;border:none;background-color:transparent;"
        scrolling="no"
        allowfullscreen="allowfullscreen"
    >
    </iframe>
    <div
        style="position:absolute;bottom:0;left:0;font-family:arial,helvetica,sans-serif;font-size:12px;line-height:1.833;display:inline-block;padding:5px 0 5px 10px;"
    ><span
            style="float:left;margin-right:10px;"><img
                style="height:20px;width:auto;background: transparent;padding:0;margin:0;"
                src="https://img2.rtve.es/css/rtve.commons/rtve.header.footer/i/logoRTVEes.png"
                alt=""
            />
        </span>
        <a
            style="color:#333;font-weight:bold;"
            title="{title}"
            href="{link}"
        >
            <strong>{title}</strong>
        </a>
    </div>
</div>
"""



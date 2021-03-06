#!/usr/bin/env python3

from pathlib import Path
from yamlns import namespace as ns
from customblocks.utils import Fetcher, PageInfo
from consolemsg import step, warn, error
from slug import slug
import json

linkfile = Path('facebook-links-2021-01.md')

linkfile_content = linkfile.read_text(encoding='utf-8')
posts = [art.strip() for art in linkfile_content.split('\n\n') if art.strip()]

def renderPost(post):
	description = "".join(
		'    '+line for line in post.description.split('\n')
		) if post.get('description','') else ''

	link = f"""\
:::linkcard {post.link} image="{post.get('image', 'NOIMAGE')}" title={repr(str(post.get('title','NOTITLE')))}
{description}
""" if 'link' in post else ''

	result = f"""\
## {post.date} {post.get('title','')}

{post.data.get('post','')}

{link}

----
"""
	return result

def renderStandAlone(post):
	description = "".join(
		'    '+line for line in post.description.split('\n')
		) if post.get('description','') else ''

	content = post.data.get('post') or post.data.get('past','') or post.get('description','')

	link = f"""\
:::linkcard {post.link} image="{post.get('image', 'NOIMAGE')}" title={repr(str(post.get('title','NOTITLE')))}
{description}
""" if 'link' in post else ''
	meta = ns(
		title = post.get('title', 'untitled'),
		date = post.date,
		status = 'published',
		original = post,
		tags = ['untagged'],
		category = '',
		location = 'España',
		author = 'vokimon',
	)

	result = f"""\
---
{meta.dump()}
---
{content}

{link}
"""
	return result


#print('\n-----\n'.join(posts))

print("Generating")

relinedPosts = []

for post in posts:
	lines = post.split('\n')
	relined = [
		reline 
		for line in lines
		for reline in line.split('. ')
	]
	repost = ns()
	if lines[-1][:4] == 'http':
		repost.link = lines.pop(-1)
	repost.post = '\n\n'.join(lines)
	relinedPosts.append(repost)

import json
import datetime
fetcher = Fetcher('remotecache')
fbexport = Path('posts_2021-01.json').read_text(encoding='utf8')
#fbexport = Path('facebook/posts/posts_1.json').read_text(encoding='utf8')
fbposts = ns.loads(fbexport)
print(len(relinedPosts), '/', len(fbposts))
for post in fbposts:
	post.date = datetime.datetime.fromtimestamp(post.timestamp, datetime.timezone.utc)
	data = ns()
	for datum in post.data:
		data.update(datum)
	post.data = data
	if not relinedPosts: continue
	handcopied = relinedPosts.pop(0)
	handcontent = handcopied.get('post','').strip()
	fbcontent = data.get('post','').strip()

	if handcontent != fbcontent:
		import difflib
		data.diff = '\n'.join(difflib.ndiff(handcontent.split('\n'), fbcontent.split('\n')))
		print('='*20)
		print(data.diff)
		data.past = handcontent

	if 'link' in handcopied:
		post.link = handcopied.link

	if 'title' in handcopied:
		post.title = handcopied.title
	elif 'link' in post:
		step("Fetching {}", post.link)
		from requests.exceptions import RequestException
		try:
			response = fetcher.get(post.link, timeout=2)
			info = PageInfo(response.text, url=post.link)
			post.title = info.title
			post.image = info.image
			post.sitename = info.sitename
			post.siteicon = info.siteicon
			post.siteurl = info.siteurl
			post.description = info.description
		except RequestException as exception:
			warn("Unable to fetch {}\n{}", post.link, exception)
	else:
		post.title = 'TittlePending'

	#print(renderPost(post))
	
	if handcontent[:5] != fbcontent[:5]:
		if handcontent and fbcontent:
			error("Masses diferencies")
			break

postdir = Path('content/articles/microblog')
postdir.mkdir(parents=True, exist_ok=True)
for post in fbposts:
	postfile = postdir / '{post.date:%Y-%m-%d-%H%M%S}-{slug}.md'.format(post=post, slug=slug(post.get('title','untitled')))
	step("Writing {}...", postfile)
	postfile.write_text(renderStandAlone(post), encoding='utf8')

ns(posts=fbposts).dump('lala.yaml')


Path('content/pages/microblog.md').write_text(
	'Title: Microblogging\n'
	'----\n' +
	'\n\n'.join(
		renderPost(post)
		for post in fbposts
	),
	encoding='utf8',
)









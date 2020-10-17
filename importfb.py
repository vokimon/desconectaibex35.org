#!/usr/bin/env python3

from pathlib import Path
from yamlns import namespace as ns
from customblocks.utils import Fetcher, PageInfo
from consolemsg import step, warn

linkfile = Path('facebook-links.md')

linkfile_content = linkfile.read_text(encoding='utf-8')
posts = [art.strip() for art in linkfile_content.split('\n\n') if art.strip()]

def renderPost(post):
	print(post.dump())
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
fbexport = Path('facebook/posts/posts_1.json').read_text(encoding='utf8')
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
	
	if handcontent[:5] != fbcontent[:5]:
		if handcontent and fbcontent:
			break


ns(posts=fbposts).dump('lala.yaml')






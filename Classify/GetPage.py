#!/usr/bin/env python
import urllib2, os
import cPickle as pickle
from ParsePage import html_to_text

CACHE_PATH = "/var/tmp/pageCache"
CACHE_PATH_B = "/var/tmp/parsedHTMLCache"

USER_AGENT = 'Mozilla/5.0'
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', USER_AGENT)]


def readURL(url):
	if not os.path.exists(CACHE_PATH):
		os.makedirs(CACHE_PATH)	
	path = None
	h = url
	if not isinstance(url,int):
		h = hash(url)		
	path = os.path.join(CACHE_PATH,str(h))
	if os.path.exists(path):
		t = None
		with open(path,"r") as f:
			t = f.read()
		return t
	elif isinstance(url,int):
		raise Exception(url,"not cached")
	
	f = opener.open(url)
	html = f.read()
	f.close()
	with open(path,"w") as out:
		out.write(html)	
	return html
	
		
def getURLText(url):
	print "getURLText:", url
	if not os.path.exists(CACHE_PATH_B):
		os.makedirs(CACHE_PATH_B)
	h = str(hash(url))
	path = os.path.join(CACHE_PATH_B,h)
	if os.path.exists(path):
		print "Loading from pickle", url
		with open(path,"rb") as f:
			return pickle.load(f)
	else:
		html = readURL(url)
		html_parsed = html_to_text(html)
		with open(path,"wb") as f:
			pickle.dump(html_parsed,f)
		return html_parsed

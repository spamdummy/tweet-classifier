#!/usr/bin/env python
import urllib2, os
import cPickle as pickle

CACHE_PATH = "/var/tmp/pageCache"
CACHE_PATH_B = "/var/tmp/parsedHTMLCache"

USER_AGENT = 'Mozilla/5.0'
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', USER_AGENT)]


def readURL(url):
	path = None
	if isinstance(url,int):
		path = "%s/%s" % (CACHE_PATH,url)
	else:
		path = "%s/%s" % (CACHE_PATH,hash(url))
	if os.path.exists(path):
		t = None
		with open(path,"r") as f:
			t = f.read()
		return t
	elif isinstance(url,int):
		raise Exception(url,"not cached")
	html = None
	with opener.open(url) as f
		html = f.read()
	with open(path,"w") as out
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

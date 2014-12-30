#!/usr/bin/env python
import urllib2, os
import cPickle as pickle
from unidecode import unidecode

CACHE_PATH = "/var/tmp/pageCache"
CACHE_PATH_B = "/var/tmp/parsedHTMLCache"
opener = urllib2.build_opener()
USER_AGENT = 'Mozilla/5.0'
opener.addheaders = [('User-agent', USER_AGENT)]


def readURL(url):
	path = None
	if isinstance(url,int):
		path = "%s/%s" % (CACHE_PATH,url)
	else:
		path = "%s/%s" % (CACHE_PATH,hash(url))
	if os.path.exists(path):
		f = open(path,"r")
		t = f.read()
		f.close()
		return t
	elif isinstance(url,int):
		raise Exception(url,"not cached")
	f = opener.open(url)
	html = f.read()
	f.close()
	out = open(path,"w")
	out.write(html)
	out.close()
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
		#html = unidecode(html)
		html_parsed = html_to_text(html)
		with open(path,"wb") as f:
			pickle.dump(html_parsed,f)
		return html_parsed

	"""
	return html_to_text(unidecode(readURL(url)))
	"""

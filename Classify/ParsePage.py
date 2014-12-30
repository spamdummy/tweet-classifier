#!/usr/bin/env python
import urllib2, re
from bs4 import BeautifulSoup as bs4
from HTMLParser import HTMLParser

TAGS = ("p","ul","li","h1","h2","h3","h4")
class MLStripper(HTMLParser):
	def __init__(self):
		self.reset()
		self.fed = []
		self.inside = False
		self.cur = ""
		self.tagStack = []
        
	def handle_starttag(self, tag, attrs):    
	#Include headers as well (h1,h2,...)
		if tag in TAGS or len(self.tagStack) > 0:	
			self.tagStack.append(tag)	        	
	def handle_endtag(self,tag):
		"""if tag in TAGS:
			self.inside = False
			self.fed.append(self.cur)
			self.cur = ""
		"""
		if len(self.tagStack) > 0:
			p = self.tagStack.pop()
			#if p != tag:
			#print p, tag
			#assert p==tag
		
	def handle_data(self, d):
		if len(self.tagStack) > 0:
			#self.cur += d
			self.fed.append(d)
	def get_data(self):
		return " ".join(self.fed)
	def get_paragraphs(self):
		return self.fed

def html_to_paragraphs(html):
	assert False and "Work in progress"
	s = MLStripper()
	s.feed(html)
	return s.get_paragraphs()
    
def _html_to_text(html):
	assert False and "Deprecated"
	s = MLStripper()
	s.feed(html)
	return s.get_data()


def html_to_text(html):
	soup = bs4(html)
	b = soup.find(id="bodyContent")
	if b:
		#wikipedia page
		return b.get_text()
	else:
		#fall back onto just grabbing all text
		return soup.get_text()

if __name__ == "__main__":
	with open("test.html","r") as f:
		t = f.read()
		print html_to_text(t)




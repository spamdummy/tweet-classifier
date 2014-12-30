#!/usr/bin/env python
import urllib2, re
from bs4 import BeautifulSoup as bs4

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




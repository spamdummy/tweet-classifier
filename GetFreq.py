#!/usr/bin/env python
import os
import cPickle as pickle
import GetPage, WordExtract
CACHE_PATH = "/var/tmp/wordFreqCache"

def setupPath():
	if not os.path.exists(CACHE_PATH):
		os.makedirs(CACHE_PATH)

def getFreq(url):
	setupPath()
	h = str(hash(url))
	path = os.path.join(CACHE_PATH, h)
	if os.path.exists(path):
		with open(path,"rb") as f:
			return pickle.load(f)
	else:
		page = GetPage.getURLText(url)
		freq = WordExtract.wordFreq(page)
		
		with open(path,"wb") as f:
			pickle.dump(freq,f)
		
		return freq
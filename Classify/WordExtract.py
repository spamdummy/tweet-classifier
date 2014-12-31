#!/usr/bin/env python
CACHE_WORD_FREQ = "/var/tmp/wordFreqCache"
CACHE_GET_WORDS = "/var/tmp/getWordsCache"
import re, os
import cPickle as pickle
from collections import defaultdict
from GetPage import getURLText
from StopWords import STOP_WORDS

def first_sentence(text):
	pos = text.find(". ")
	if pos!=-1:
		return text[:pos+2]
	else:
		return text
		
def getWords_weighted(paragraphs):
	pass

def remove_urls(text):
	return re.sub("https?://[^\s]+","",text)
	
def getWords(text):
	assert type(text) in (str,unicode)
	text = remove_urls(text)
	words = re.findall("[a-z]{2,}",text,re.I)	
	#make everything lowercase.
	words = map(lambda x:x.lower(),words)
	#filter out stop words
	return [word for word in words if word not in STOP_WORDS]



def __(url,dir,func):
	if not os.path.exists(dir):
		os.makedirs(dir)
	path = os.path.join(dir,str(hash(url)))	
	if os.path.exists(path):
		with open(path,"rb") as f:
			return pickle.load(f)
	else:
		with open(path,"wb") as fp:
			text = getURLText(url)
			return func(text,fp)

def getWordsByURL(url):	
	def func(text,fp):
		words = getWords(text)
		pickle.dump(words,fp)
		return words
	return __(url,CACHE_GET_WORDS,func)

def wordFreqByURL(url):
	def func(text,fp):
		count = wordFreq(text)
		pickle.dump(count,fp)
		return count	
	return __(url,CACHE_WORD_FREQ,func)

	
def wordFreq(text):	
	words = getWords(text)
	count = defaultdict(int)
	for word in words:
		count[word] += 1	
	return count

def smartLowerCase(string):
	"""
	Distinguish uppercase acronyms
	E.g. IT (information tech)	
	if string.isupper():
		return string
	else:
		return string.lower()
	"""
	return string.lower()
	
def test():
	text = """
	Hello World
	https://twitter.com/This_shouldnt_be_visible
	http://twitter.com/This_shouldnt_be_visible
	"""	
	print remove_urls(text)
if __name__ == "__main__":
	test()
#!/usr/bin/env python
import urllib2, re, os, random
from fractions import Fraction
from pprint import pprint
import CrossValidate
from WordExtract import wordFreqByURL, getWordsByURL
from GetPage import getURLText
from GetFreq import getFreq
from Classify import TextClassifier
data = {
	"science":[		
		"http://en.wikipedia.org/wiki/Science",
		"http://en.wikipedia.org/wiki/Branches_of_science",
		"http://en.wikipedia.org/wiki/Outline_of_science",
		"http://en.wikipedia.org/wiki/Outline_of_natural_science",
		"http://en.wikipedia.org/wiki/Outline_of_physical_science",
		"http://en.wikipedia.org/wiki/Outline_of_earth_science",
		"http://en.wikipedia.org/wiki/Outline_of_applied_science",
		
		"http://en.wikipedia.org/wiki/Mathematics",
		
		"http://en.wikipedia.org/wiki/Biology",
		"http://en.wikipedia.org/wiki/Chemistry",
		"http://en.wikipedia.org/wiki/Physics",
		"http://en.wikipedia.org/wiki/Geology",
		
		"http://en.wikipedia.org/wiki/Oceanography",
		"http://en.wikipedia.org/wiki/Paleontology",
		"http://en.wikipedia.org/wiki/Geochemistry",
		
		"http://en.wikipedia.org/wiki/Engineering",
		
		"http://en.wikipedia.org/wiki/Bill_Nye",
		"http://en.wikipedia.org/wiki/Neil_deGrasse_Tyson",
		"http://en.wikipedia.org/wiki/Karl_Kruszelnicki",
		
		"http://en.wikipedia.org/wiki/Science_journalism",
		"http://en.wikipedia.org/wiki/List_of_scientific_journals",					
	],	
	"other":[	
		"http://en.wikipedia.org/wiki/Kim_Kardashian",
		"http://en.wikipedia.org/wiki/Jay-Z",
		"http://en.wikipedia.org/wiki/Mos_Def",
		"http://en.wikipedia.org/wiki/Music_video",
		"http://en.wikipedia.org/wiki/MTV",		
		"http://en.wikipedia.org/wiki/Olympic_Games",
		"http://en.wikipedia.org/wiki/National_Basketball_Association",
		"http://en.wikipedia.org/wiki/FIFA",
		"http://en.wikipedia.org/wiki/CrossFit",		
				
		"http://en.wikipedia.org/wiki/The_Simpsons",						
		
		"http://en.wikipedia.org/wiki/Call_of_Duty",
		"http://en.wikipedia.org/wiki/BuzzFeed",

	],
}

def getClassifier():
	classifier = TextClassifier()
	for category,urls in data.items():
		for url in urls:
			classifier.train(wordFreqByURL(url),category)
	return classifier
	
def test():
	#convert the mapping of categories and urls 
	#to a list of tuples
	_a = []
	for category, urls in data.items():
		for url in urls:
			_a.append((category,url))
	random.shuffle(_a)

	p = CrossValidate.partition(_a,int(0.2 * len(_a)))
	totalScore = 0
	for k in p:
		classifier = TextClassifier()
		for partition in p:
			if k != partition:
				for category, url in partition:						
					classifier.train(wordFreqByURL(url),category)
		score = 0
		for category,url in k:
			classification = classifier.classify(getWordsByURL(url))

			if classification == category:
				score +=1
			else:
				print "WRONG", url, classification
		frac = Fraction(score,len(k))
		totalScore += Fraction(frac,len(p))
		#print "Score: %s" % frac
	print "Classification score: %s" % totalScore 	

if __name__ == "__main__":
	test()
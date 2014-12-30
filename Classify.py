#!/usr/bin/env python
import math, re
from collections import defaultdict
from fractions import Fraction
from WordExtract import getWords, wordFreq


class TextClassifier:
	"""
	Naive Bayes Classifier	
	(multinomial model) - based on frequency of words
	"""
	def __init__(self):
		self.classes = defaultdict(lambda : defaultdict(int))
		self.totalSamples = 0		
		self.vocabs = {}
	def topWords(self,className,numWords=20):
		d = self.classes[className]
		k = sorted(d,key=d.get,reverse=True)
		for i in k[:numWords]:
			print i, d[i]
		
	def train(self,obj,className):
		freqs = None
		if isinstance(obj,str) or isinstance(obj,unicode):
			freqs = wordFreq(obj)			
		elif isinstance(obj,dict):
			freqs = obj			 
		else:
			raise Exception("Obj must be text or word-freqs dict")			
		for word, freq in freqs.items():	
			self.classes[className][word] += freq 	
			
	def allWords(self):
		vocab = set()
		for freqMaps in self.classes.values():
			vocab = vocab.union(freqMaps.keys())
		return sorted(vocab)
			
	def computeProb(self,obj,className):
		words = None
		if type(obj) in (str,unicode):		
			words = getWords(obj)
		else:
			words = obj
		nWords = sum(self.classes[className].values())
		logSum = 0
		for word in words:
			freq = self.classes[className][word] + 1
			prob = Fraction(freq,nWords)
			logSum += math.log(prob)
		return logSum
	
	def classify(self,obj,verbose=False):
		probs = {}
		for className in self.classes:
			probs[className] = self.computeProb(obj,className)
		
		highestClass = sorted(probs,key=probs.get)[-1]
		highest = probs[highestClass]
		if verbose:
			print probs
			#print (obj[:100], highestClass, highest)
		return highestClass
			

FOOD = "food"
TECH = "tech"
def test():
	a = TextClassifier()	
	a.train("Apple fish ",FOOD)
	a.train("fish steak",FOOD)	
	a.train("Computer software",TECH)	 
	a.train("app Apple",TECH)
	print a.allWords()
	print a.classes
	print a.computeProb("apple",FOOD)
	print a.computeProb("apple",TECH)	
	print a.computeProb("fish",FOOD)
	print a.computeProb("fish",TECH)
	assert a.classify("fish") == FOOD
	assert a.classify("software") == TECH
	
if __name__ == "__main__":
	test()		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
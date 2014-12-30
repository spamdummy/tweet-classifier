#!/usr/bin/env python
#http://en.wikipedia.org/wiki/Cross-validation_(statistics)
from __future__ import division 
import math, random

ceil = lambda x:int(math.ceil(x))
def partition(arr, chunkSize):
	c = chunkSize
	return [ arr[x*c:(x+1)*c] for x in range(ceil(len(arr)/c))]

def flatten(arr_of_lists):
	a = arr_of_lists
	out = []
	for _list in a:
		out += _list
	return out

def test():
	#fuzz testing
	for g in range(10000):
		x,y = random.randint(0,100),random.randint(1,100)
		z = flatten(partition(range(x),y))		
		assert z == range(x) 

if __name__ == "__main__":
	test()
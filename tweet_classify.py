#!/usr/bin/env python
from GetPage import getURLText
from ScienceTweetClassifier import getClassifier
data = {
	"science":[
		"These dazzling light sculptures will test your sense of reality",
		"New research might explain why some people survive Ebola while others do not ",
		"China's lunar rover has sent some wonderful new pics back from the moon. ",
		
	],
	"other":[
		"Here are 15 essential apps to install on your new iPad ",
		"AirAsia Flight 8501 and what makes thunderstorms such a threat to airliners "
	]
	
}

c = getClassifier()

for category,tweets in data.items():
	for tweet in tweets:
		_class = c.classify(tweet,verbose=True)
		rating = "Correct." if _class == category else "Wrong!"
		print "%s [%s]. Classified as %s" % (rating,tweet,_class) 
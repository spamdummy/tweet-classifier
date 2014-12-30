#!/usr/bin/env python
from Classify.TextClassifier import TextClassifier
from Classify.GetPage import getURLText
training_data = {
	"sport":[
		"http://en.wikipedia.org/wiki/Sport",
		"http://en.wikipedia.org/wiki/List_of_sports",
		
	],
	"food":[
		"http://en.wikipedia.org/wiki/food",
		"http://en.wikipedia.org/wiki/Sandwich",
	]
	
}

#new TextClassifier instance
t = TextClassifier() 

#train the classifier using the training data
for category,urls in training_data.items():
	for url in urls:
		t.train(getURLText(url),category)

#now we can use the classifier!
print t.classify("Sorry grilled cheese sandwiches, we've moved on to grilled chocolate sandwiches.")
print t.classify("Arkansas defense suffocates Texas in 31-7 win.")

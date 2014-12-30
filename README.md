tweet-classify
==============
This project aims to classify Tweets as science or non-science related.
The ScienceClassifier is a trained version of the generic TextClassifier.
The TextClassifier uses the [Multinomial Naive Bayes](http://en.wikipedia.org/wiki/Naive_Bayes_classifier#Multinomial_naive_Bayes) model.
All code so far is in [Python](https://www.python.org/).

##Dependencies
* [Beautiful Soup 4](http://www.crummy.com/software/BeautifulSoup/)

##Examples:
###Science Classifier
```python
#To use the science text classifier
from Classify.ScienceClassifier import getClassifier

c = getClassifier()

#prints 'science'
print c.classify(
"""Newton's laws of motion are three physical laws that together
laid the foundation for classical mechanics."""
)

#prints 'other'
print c.classify(
"""A disc jockey (abbreviated D.J., DJ or deejay) is a person 
who mixes recorded music for an audience; in a club event 
or rave, this is an audience of dancers."""
)
```
Examples text from Wikipedia: [Newton's Laws](http://en.wikipedia.org/wiki/Newton%27s_laws_of_motion), [DJ](http://en.wikipedia.org/wiki/Disc_jockey).
###Generic Text Classifier
```python
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

#now we can put the classifier into action. Here we are classifying some tweets!
print t.classify("Sorry grilled cheese sandwiches, we've moved on to grilled chocolate sandwiches.")
print t.classify("Arkansas defense suffocates Texas in 31-7 win.")
```

##The Details
Calling GetPage.getURLText grabs a webpage's text.
The cPickle class is used for caching.
At the moment cached webpages are stored in /var/tmp (this may be an issue for Windows users?) 

##Attributions
* [Python](https://www.python.org/)
* [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/)
* [StopWords](http://www.ranks.nl/stopwords/)
* [Wikipedia](http://www.en.wikipedia.org)
* [Twitter](https://twitter.com/)
* Tweets: [a tweet on food](https://twitter.com/foodandwine/status/549278672109056001) and [a tweet on sport](https://twitter.com/SECfootball/status/549808451652579328)


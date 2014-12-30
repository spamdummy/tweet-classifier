tweet-classify
==============
Includes a general Text Classification class.
The science specific text classifier (ScienceClassifier) is a trained version of the generic TextClassifier.

##Examples:
###Science Classifier
```
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
"""MTV (an initialism of music television) is an American basic cable and 
satellite television channel owned by the MTV Networks Music & Logo Group, 
a unit of the Viacom Media Networks division of Viacom. """
)
```
###Generic Text Classifier
```
#todo
```

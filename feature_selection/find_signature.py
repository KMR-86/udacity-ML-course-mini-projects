#!/usr/bin/python

import pickle
import numpy
from sklearn.model_selection import cross_validate
from sklearn.model_selection import train_test_split
numpy.random.seed(42)
from sklearn import linear_model
clf = linear_model.Lasso()

from sklearn.feature_extraction.text import TfidfTransformer

### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "../text_learning/your_word_data.pkl" 
authors_file = "../text_learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "rb"))
authors = pickle.load( open(authors_file, "rb") )



### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier

features_train, features_test, labels_train, labels_test = train_test_split(word_data, authors, test_size=0.1, random_state=42)


from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')

features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()


### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)
acc=clf.score(features_test,labels_test)
print(acc)
### your code goes here

all_features=vectorizer.get_feature_names()


print(features_train)
feature_importance=clf.feature_importances_
print(feature_importance)



count = 0
all_list=[]

for importance in feature_importance:
    if importance >= 0.2:
        print(count,importance,vectorizer.get_feature_names()[count])
        all_list.append([count,importance,vectorizer.get_feature_names()[count]])
    count +=1

all_list=sorted(all_list,key = lambda x: x[2],reverse=True)
print(all_list)
print(len(all_list))
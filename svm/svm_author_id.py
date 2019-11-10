#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

from sklearn import svm
clf=svm.SVC(kernel='rbf',C=10000.0)

#features_train = features_train[:round(len(features_train)/100)]  #making the data smaller to reduce the run time
#labels_train = labels_train[:round(len(labels_train)/100)]        #but this will also drop the accuracy
#features_test = features_test[:round(len(features_test))]  #making the data smaller to reduce the run time
#labels_test = labels_test[:round(len(labels_test))]
clf.fit(features_train,labels_train)
score=clf.score(features_test,labels_test)
pred=clf.predict(features_test)
count=0
for i in range(0,len(pred)):
    if pred[i]==1:
        count=count+1
print(score)
print(count,len(pred))
#########################################################



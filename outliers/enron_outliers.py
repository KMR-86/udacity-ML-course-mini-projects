#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
import numpy
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "rb") )
print(data_dict)
#data_dict.pop("TOTAL",0)
#print(data_dict)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)
print("data size",data.shape)
#,sort_keys = '../tools/python2_lesson06_keys.pkl'
salary_data,bonus_data = targetFeatureSplit( data )
temp=[]
for item in salary_data:
    temp.append(numpy.array([item]))
salary_data=temp


data=sorted(data, key=lambda x:x[1],reverse=True)
print(data)
outliner_bonus=data[0][1]
for key,item in data_dict.items():
    #print(float(item['bonus']),"   ",outliner_bonus)
    if float(item['bonus'])==outliner_bonus:
        print(key,"   ",)
        break






for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )




matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

### this code below was my unsuccessful attempt


#print("salary list",salary_data)
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(salary_data,bonus_data)
predictions = reg.predict(salary_data)


diff=abs(predictions-bonus_data)


#print("the difference data",diff)
list_of_target_and_err=[]

for i in range(0,len(diff)):
    list_of_target_and_err.append([bonus_data[i],diff[i]])

list_of_target_and_err.sort(key=lambda tup: tup[1])
outliner_bonus=list_of_target_and_err[len(list_of_target_and_err)-1][0]
#print(outliner_bonus)

for key,item in data_dict.items():
    if float(item['bonus'])==float(outliner_bonus):
        #print(key,"   ",list_of_target_and_err[len(list_of_target_and_err)-1])
        print(".")
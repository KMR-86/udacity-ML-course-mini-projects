#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "rb") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)


### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
poi  = "poi"
features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )
salary_list=[]
ex_stock_op_list=[]
for item in finance_features:
    salary_list.append(numpy.array([item[0]]))
    ex_stock_op_list.append(numpy.array([item[1]]))



print((200000.0-min(salary_list))/(max(salary_list)-min(salary_list)))
print((1000000-min(ex_stock_op_list))/(max(ex_stock_op_list)-min(ex_stock_op_list)))
finance_features=sorted(finance_features,key=lambda x:x[0])
print(finance_features)

finance_features=sorted(finance_features,key=lambda x:x[0],reverse=True)
print(finance_features)

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scalled_salary_list=scaler.fit_transform(salary_list)
#print(scalled_salary_list)

scalled_ex_stock_op_list=scaler.fit_transform(ex_stock_op_list)
#print(scalled_ex_stock_op_list)


#wrong attempt
'''for i in range(0,len(finance_features)):
    print(finance_features[i][0],"    ",finance_features[i][1])

    if finance_features[i][0]==200000.0 and finance_features[i][1]==1000000.0:
        print("salary ",scalled_salary_list[i])
        print("stock op ",scalled_ex_stock_op_list[i])'''
#wrong attempt

### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
for f1, f2  in finance_features:
    plt.scatter( f1, f2 )
plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2, random_state=0).fit(finance_features)
pred=kmeans.predict(finance_features)

### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="my_clusters_after_scalling.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print("no predictions object named pred found, no clusters to plot")

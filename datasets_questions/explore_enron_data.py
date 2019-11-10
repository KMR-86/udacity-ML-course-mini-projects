#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
count=0
poi_count=0
total_payment_count=0
total_poi_with_no_salaty=0
money_set=set()
salary_list=[]
email_count=0
for man in enron_data:
    count=count+1
    #print(enron_data[man]," length is ",len(enron_data[man]))
    if enron_data[man]["poi"]==1:
        poi_count=poi_count+1
    print(enron_data[man])
    if man=="SKILLING JEFFREY K":
        print(enron_data[man]["exercised_stock_options"])

    if enron_data[man]["total_payments"]!="NaN":
        money_set.add(int(enron_data[man]["total_payments"]))

    if enron_data[man]["salary"]!="NaN":
        salary_list.append(int(enron_data[man]["salary"]))
    if enron_data[man]["email_address"]!="NaN":   
        email_count=email_count+1

    if enron_data[man]["total_payments"]!="NaN":
        total_payment_count=total_payment_count+1
    
    if enron_data[man]["total_payments"]=="NaN" and  enron_data[man]["poi"]==1:
        total_poi_with_no_salaty=total_poi_with_no_salaty+1

print("total number of people",count)
print("full money set",sorted(money_set))
print("the number of employees with real salary",len(salary_list))
print("the number of employees with real total payment",total_payment_count)
print("the number of employees with real email",email_count)
print("maximum money in the list",max(money_set)) #that's actually total money
print(poi_count)
print(1-total_payment_count/count)
print(total_poi_with_no_salaty/poi_count)


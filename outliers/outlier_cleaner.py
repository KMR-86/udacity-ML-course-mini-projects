#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    print("predictions: ",predictions)
    print("net_worths: ",net_worths)
    diff=abs(predictions-net_worths)
    print(diff)
    list=[]
    for i in range(0,len(diff)):
        list.append([ int(ages[i]), float(net_worths[i]), float(diff[i])])

    print(list)

    list.sort(key=lambda tup: tup[2])
    print(list)
    cleaned_data = []
    for i in range(0,80):
        cleaned_data.append(list[i])

    ### your code goes here

    
    return cleaned_data


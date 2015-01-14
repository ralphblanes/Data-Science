__author__ = 'ralphblanes'
import random
import math
import scipy
import csv as csv
import numpy as np
import pandas

data = pandas.read_csv(('./Data/Titanic/titanic_train.csv'))
data = data.as_matrix()
data = data[::,0:13]

gender = data[::,4]
men = gender == 'male'
women = gender !='male'
#These are masks
print data[1,1]

fare_ceiling = 40
data[data[::,9].astype(np.float)>=fare_ceiling] = fare_ceiling-1.0
#Making a ceiling

bin_size = 10
fare_bracket_size = fare_ceiling/bin_size
number_of_classes = len(np.unique(data[0::,2]))

survival_table = np.zeros((2,number_of_classes,fare_bracket_size))
for i in xrange(number_of_classes):
    for j in xrange(fare_bracket_size):
        women_only_stats = data[                          \
                         (data[0::,4] == "female")    \
                       &(data[0::,2].astype(np.float) \
                             == i+1) \
                       &(data[0:,9].astype(np.float)  \
                            >= j*fare_bracket_size)   \
                       &(data[0:,9].astype(np.float)  \
                            < (j+1)*fare_bracket_size)\
                          , 1]


        men_only_stats = data[                            \
                         (data[0::,4] != "female")    \
                       &(data[0::,2].astype(np.float) \
                             == i+1)                  \
                       &(data[0:,9].astype(np.float)  \
                            >= j*fare_bracket_size)   \
                       &(data[0:,9].astype(np.float)  \
                            < (j+1)*fare_bracket_size)\
                          , 1]

survival_table[0,i,j] = np.mean(women_only_stats.astype(np.float))
survival_table[1,i,j] = np.mean(men_only_stats.astype(np.float))
def binarySearch(array,number,start_index):
    """
    #:param array(sorted array of integers), number(number to find the index of)
    #:return int:index -> The index of the number

    """
    if len(array) == 0:
        return -1
    elif len(array) == 1:
        if array[0] == number:
            return start_index
        else:
            return -1
    else:
        first_partition = array[start_index:len(array)/2]
        print "first part"
        print first_partition
        last_partition = array[len(array)/2:len(array)+1]
        print "last part"
        print last_partition
        first_return = binarySearch(first_partition,number,start_index)
        print "first recurse"
        print first_return
        second_return = binarySearch(last_partition,number,len(array)/2)
        print "second recurse"
        print second_return
        if first_return == -1 == second_return:
            return -1
        elif first_return != -1:
            return first_return
        elif second_return != -1:
            return second_return
        else:
            return -1












def generateSortedArrays(number_of_elements, biggest_number):
    return_array = []
    for i in range(0,number_of_elements):
        return_array.append(random.randint(0,biggest_number))
    return_array.sort()
    return return_array



arr = []
dice = [1,2,3,4]
for i in range(1,5):
    for j in dice:
        arr.append(float((j+i))/2)
print arr
print sum(arr)/len(arr)

def czc(number,mean,dev):
    return float(number-mean)/dev

print czc(3,2.5,0.8175)
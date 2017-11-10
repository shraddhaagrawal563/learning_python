# -*- coding: utf-8 -*-
#https://www.tutorialspoint.com/numpy/numpy_array_attributes.htm
import numpy as np 
x = np.array([1,2,3,4,5]) 
print ("item size" , x.itemsize) #prints size of an individual element

x = np.array([1,2,3,4,5,4.2,3.6]) 
print ("item size" , x.itemsize) #converts every element to the largest of size

x = np.array([1,2,3,4,5,3.3,"str"]) 
print ("item size" , x.itemsize)

x = np.array(["a","b", 4.5]) #adding size of each type
print ("item size" , x.itemsize)

''' only similar datatypes element can be put 
inside an numpy array.. the above thing is not practised'''
print("\nnumpy flags")
x = np.array([1,2,3,4,5]) 
print ("item size" , x.flags) #gives the complete state of array
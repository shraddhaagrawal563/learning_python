# -*- coding: utf-8 -*-
#numpy is python package
#array creation
import numpy as np
print("creating numpy array")
arr=np.array([1,2,3,4]) #array generation , coverting list to array
print("numpy array is", arr)
print("numpy array type" , type(arr)) #array is a class in numpy

lst=[1,2,3,4]
arr2= np.array(lst)
print("array is:", arr2)

arr3= np.array(33)
print("array is:", arr3)

#built in array function takes only one object as arguement, so following stmt will throw erroe
#np.array(object,dtype,copy......)
#object could be type, sequence, nested sequence
#arr2= np.array(22,1)   
#print("array is:", arr2)

print("array from a tuple")
tpl1=(1,2,3,4)
arrtp1=np.array(tpl1,dtype=np.int16)
arrtp2=np.array(tpl1,dtype=float) #array generation , coverting list to array
print("numpy array is", arrtp1)
print("numpy array is", arrtp2)

print("array with multiple datastructures")
data=[[4,5,6],(1,2,3,4)]
arrmul=np.array(data)
print("numpy array is", arrmul)

print("array with multidimensional")
data=[[4,5,6],[1,2,3,4]]
arrmul=np.array(data)
print("numpy array is", arrmul)

print("array with multiple datastructures")
data=[[4,5,6],[1,2,3,4]]
arrmul=np.array(data, dtype=complex)
print("numpy array is", arrmul)


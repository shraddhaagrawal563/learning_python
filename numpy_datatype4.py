# -*- coding: utf-8 -*-
#https://www.tutorialspoint.com/numpy/numpy_array_attributes.htm
#transpose program and reshaping program
import numpy as np 
a = np.array([[1,2,3],[4,5,6]]) 
print("original array:", a)
print (a.shape) # 2 rows and 3 column

print("\narray transpose:", a.T) # transpose is diffrent from reshape

print("changing the shape of array")
a.shape=(3,2) # 3 rows and 2 columns
print("reshaped array:", a)
print ("array reshaped",a.shape)

print("\nchanging the shape of array without altering original")
b = a.reshape(2,3) #array a remains unchanged by reshape function
print("reshaped array:", b)
print ("original array shape:",a.shape)
print ("reshaped array shape:",b.shape)

print("dimension of a", a.ndim) #both are 2d array
print("dimension of b", b.ndim) 
print("ndim represents the dimension of array, not rows and columns")

print("dealing with range which creates 1d array\n")
a = np.arange(24) #makes a linear list
print("array is " ,a) 
print("dimension of a", a.ndim)
print("shape of array" , a.shape)  
# now reshape it 
print("\ndealing with 3d array byreshaping 1d")
b = a.reshape(2,4,3) 
print("array is", b)
print("dimension of b", b.ndim) 

zeromul= np.zeros([2,3]) #float values as outout by default
print("zero array", zeromul)

zeromul= np.zeros([2,3], dtype=int) #dtype as int
print("zero array with int dtype", zeromul)

zeromul1=np.zeros_like(b)
print("zero array with same attributes as A", zeromul1)

onesmul= np.ones([2,3]) #float values as outout by default
print("ones array", onesmul)

print("as array demo")
lst=[7,55,22,69]
print("list", lst)
asarr=np.asarray(lst,dtype=np.int16)
print("asarray", asarr) #displayes list as an array

print("array from buffer")
arrbfr= np.frombuffer(b"datascience",dtype='S1') #strings are stores in buffer
print("buffer array", arrbfr) #interprets buffer as 1d array
#dtype mentions element size in arrbfr

list = range(5) 
it = iter(list)  
# use iterator to create ndarray 
x = np.fromiter(it, dtype=float) 
print (x)








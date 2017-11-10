# -*- coding: utf-8 -*-
#series
import pandas as pd
import numpy as np
print("creating empty series")
emptyser= pd.Series() #s should be capital in Series
print("empty series is", emptyser)

"""
series-- size immutable, data mutable, homogenous
"""


print("creating series from ndarray")
data=[12,34,56,76]
data= np.array(data)
print("data is", data)

ser=pd.Series(data)
print("the series is\n",ser)

lendata= len(data)
lst = [i for i in range(lendata)] #list comprehension- making whole list in one line
print("index used:", lst) #if we dont give index then by default range function is used

print("manual index specification")
ser2= pd.Series(['a','b','c','d'], index=[101,102,103,104]) #indexes are used to make extraction of data simple
print("series is\n", ser2)

ls=[]
for i in range(4):
    ls.append(i)
print("ls by for loop: ",ls) #list comprehension saves us from writing these 4 lines 


lst = [i for i in range(10) if i%2==0] #a chnage in list comprehension
print(lst)

f=lambda x,y: x+y;
print(f(1,2))
"""
lamba function is one lined function, with arg, with return type
"""

print("creating a series from a dictionary")
lst=[{10,"data1"},{11,"data2"}]
dict1= dict(lst)
print("dictionary is", dict1)
ser3= pd.Series(dict1)
print("series from dict is", ser3)

print("\naltering series")
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
print ("filled missing values in series (nan for d)", s)

print("series from scalar")
data=5
scalarser=pd.Series(data, index=[45,56,2])
print("sacalar sereies is", scalarser)



# -*- coding: utf-8 -*-
#series
import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print("series s is\n" , s)

print("\naccessing series element")
print("s[2]=", s[2]) #just like array 2nd element
print("\ns[0:2]=\n", s[0:2]) #from 0 to 2 excluding 2
print("s[:]=\n", s[:]) #complete series
print("s[-2:]=\n", s[-2:]) #from -2 till end
print("s[-2]=\n", s[-2]) #last second element
print("s[-2:-1]=\n", s[-2:-1]) #5th element
print("s[a]=", s['a']) #corresponding value of label




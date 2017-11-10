# -*- coding: utf-8 -*-
import numpy as np
dt= np.dtype([('age',np.int8)])
a=np.array([(10,),(20,),(30,)]) #here there are 3 tuples in a list
print("printing 10 from array", a[0][0])
''' here first [] indicates the list index 
and 2nd [] indicates the index of tuple 
(first member) in list''' 
print("array is:" , a)
print("dt[\'age\']:", dt['age'])

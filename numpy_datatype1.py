# -*- coding: utf-8 -*-
''' names for int8, int16, int32, int64 and so on'''
import numpy as np

dt = np.dtype(np.int32) #creating our own datatypes
print("numpy int type:", dt) #reusable name

dt1= np.dtype('i1') #2nd way of creating user defined dtype
print("i1 dt",dt1)

dt2= np.dtype('i2')
print("i2 dt",dt2)

dt3= np.dtype('i4')
print("i3 dt",dt3)

dt4= np.dtype('i8')
print("i4 dt",dt4)



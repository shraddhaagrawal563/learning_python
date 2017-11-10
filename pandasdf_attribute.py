# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
print("creating dataframes from series")
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("Our data series is:")
print (df)
print("transpose of df:", df.T)
print("axes of df:", df.axes)
print("dtype of df:", df.dtypes) #dtypes is used with hetrogeneous data structures
print("dimension of df:", df.ndim)
print("shape of df:", df.shape)
print("values of df:\n", df.values)
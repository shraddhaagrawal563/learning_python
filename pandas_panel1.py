# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

print("creating panel from ndarray")
data = np.random.rand(2,4,5)
p = pd.Panel(data)
print(p)

"""
size isthe output
2 items, 4 rows,5 columns
"""
print("\ncreating panel from dataframes")
pd1=pd.DataFrame(np.random.randn(4, 3)) 
pd2=pd.DataFrame(np.random.randn(4, 2))
print("pd1 sample", pd1.head()) #head function to extract first five rows 
print("pd2 sample", pd2.head())

print("\ncreating panel from dict")
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print ("panel data from dict:" ,p)

print(data['item1'])
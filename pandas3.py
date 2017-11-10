# -*- coding: utf-8 -*-
#dataframes
#rows called as intance and columns are called schemas
import pandas as pd
print("empty dataframe")
emptydf= pd.DataFrame()
print("empty df:", emptydf)

print("dataframe from list")
lst=[1,2,3,4,5,6,7]
lstdf = pd.DataFrame(lst)
print("lstdf:\n", lstdf) #an extra 0 at the top represents 2d that is column

print("df from list of list")
data = [['Alex',10],['Bob',12],['Clarke',13]]
loldf = pd.DataFrame(data,columns=['Name','Age'],dtype=float) 
print("loldf:\n", loldf)

data = {'Name1':'Tom','name2':'Jack'}
print("dictionary is", data)
dictdf1= pd.DataFrame(data, index=(19,20)) #specifying index b3comes madatory when we convert dict to df
print("dictdf1:\n", dictdf1)


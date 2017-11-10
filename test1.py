# -*- coding: utf-8 -*-
l1 = [1,2,5,7]
#l1=l2
l2=l1
l1[3]=28
print("l2[3]:", l2[3])

"""
here it is shallow copy



in python 2.7, dictionary elements got printed randomly, but in python
3.6 it gets pr
"""
#x='string'
x=3
def show(x):
    print("x=",x)
show(x)
print(x)    
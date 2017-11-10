# -*- coding: utf-8 -*-
def numprint(val):
    if val<0:
        raise "invalid argument"  #raise for exceptional handling
    print(val)    

numprint(-1)
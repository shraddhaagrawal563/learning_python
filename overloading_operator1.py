# -*- coding: utf-8 -*-
#overloading print for a class
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        
    def __str__(self):    #overloads print function for printing object
        return "({0},{1})".format(self.x,self.y) #formats output
    
    
p=Point(2,3)
print(p)    
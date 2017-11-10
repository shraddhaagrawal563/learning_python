# -*- coding: utf-8 -*-
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        
    def __str__(self):    #overloads print function for printing object
        return "({0},{1})".format(self.x,self.y) #formats output
    
    def __eq__(self,other):
        return self==other
    
    def __lt__(self,other):
        a=self.x+other.x      # writing code for addition manually
        b=self.y+other.y
        return a<b
    
        
    
p1=Point(2,3)
p2=Point(3,4)
print(p1<p2)
print(p1==p2)

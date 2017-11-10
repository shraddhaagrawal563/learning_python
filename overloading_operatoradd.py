# -*- coding: utf-8 -*-
#overloading + operator for a class
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        
    def __str__(self):    #overloads print function for printing object
        return "({0},{1})".format(self.x,self.y) #formats output
    
    def __add__(self,other):
        x=self.x+other.x      # writing code for addition manually
        y=self.y+other.y
        return Point(x,y)
        
    
p1=Point(2,3)
p2=Point(3,4)
p3=p1+p2   #this stmt internally calls p1.__add__(p2)
print(p3)  #p3 is of type: Point 
print(p1.__add__(p2))   #p2 is atual argument whereas other is formal

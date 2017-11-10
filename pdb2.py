# -*- coding: utf-8 -*-
import random
import pdb
def display_list(li):
    #clear the screen
    print("\n"*10)
    for value in li:
        print("**"*value)
    #pause untill the user hits enter
    input("**=>HIT enter")
    
def bubblesort(li):
    "sorts l in place and return it"
    for passesleft in range(len(li)-1,0,-1):
        for index in range(passesleft):
            if li[index]<li[index+1]:
                li[index],li[index+1]=li[index+1],li[index]
        display_list(li)
        return li
lst1=[random.randrange(1,50) for i in range(1,20)]
print("the input list is", lst1)
input("hit enter")
pdb.set_trace()
bubblesort(lst1)
print(lst1)        

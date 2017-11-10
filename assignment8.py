# -*- coding: utf-8 -*-
str1 ='madam'
print("string is:", str1)
#print(list(str1))
revstr1 = str(reversed(str1)) #built in function to reverse string
print("reversed object:",revstr1) #reversed function returns an object
#print(list(revstr1)) 
if list(str1) == list(revstr1): #so we convert it to list
    print("string is a plaindrom")
else:
    print("not a palindrom")
          
str2 ='madaM'
print("\nstring is:", str2)
str2 = str2.casefold() #coverts to lowercase to ignore case difference
print("string converted to lower case:",str2) 
revstr2 = reversed(str2) #built in function to reverse string
if list(str2) == list(revstr2): 
    print("string is a palindrom")
else:
    print("not a palindrom")      
    

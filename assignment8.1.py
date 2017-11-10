# -*- coding: utf-8 -*-
str1 ='madam'
print("string is:", str1)
print(list(str1))
revstr1 = reversed(str1) #built in function to reverse string
print("reversed object:",revstr1) #reversed function returns an object
print(list(revstr1)) 
if list(str1) == list(revstr1): #so we convert it to list
    print("string is a plaindrom")
else:
    print("not a palindrom")

# -*- coding: utf-8 -*-
from timeit import default_timer as timer #from timeit class import default_timer function

start = timer()
print("hello world")
end = timer()
print(end - start)   #gives execution time in positive
#print(start - end)  #gives execution time in negative


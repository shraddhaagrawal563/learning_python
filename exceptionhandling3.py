# -*- coding: utf-8 -*-
import abc

try:
    f1=open("abc.doc",'r')    #multiple excepts can be used
except (IOError,ImportError):
    print("error may be import or IO")
except exception as ex:
    print(ex)
except:
    print("an exception")
else:
    print("file opened successfully")    #will execute if try and except doesnot execute
#finally block will execute irrespective of conditions 
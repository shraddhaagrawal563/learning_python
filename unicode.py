# -*- coding: utf-8 -*-
'''
string: sequence of bytes
each element: 1 byte size= length of string
text: sequence of code points
code point size: may be greater than one byte
text can be encoded to specific type(code scheme)
unicode:general rep of some text which can be encoded in diffrent ways
'''
#https://stackoverflow.com/questions/18034272/python-str-vs-unicode-types
print(len(u'à'))  # a single code point
print(len('à'))   # by default utf-8 -> takes two bytes
print(len(u'à'.encode('utf-8')))
len(u'à'.encode('latin1'))  # in latin1 it takes one byte
print (u'à'.encode('utf-8'))  # terminal encoding is utf-8
print (u'à'.encode('latin1')) #2 bytes size
'''
unicode converted to diffrent types and size
in python 3, str is a unicode string
unicode - each text element has its unique code'''
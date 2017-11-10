# -*- coding: utf-8 -*-
#creating a datatype from primilanary type
#two ways to create datatype
import numpy as np
print("creating a datatype from primilanary np type")
dt=np.dtype(np.int64)
print("datatype dt is", dt)
print("other way to create datatype")
dt=np.dtype('i4')
print("data type dt is:", dt)

print("big endian assignment")
dt=np.dtype('>i4')
print("data type in big endian dt is:", dt)

print("little endian assignment")
dt=np.dtype('<i4')
print("data type in little endian dt is:", dt)


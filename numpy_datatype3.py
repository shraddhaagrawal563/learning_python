# -*- coding: utf-8 -*-
#creating a structured datatype
import numpy as np
print("creating a structured datatype")
dt=np.dtype([('age',np.int64)])
print("datatype dt is", dt)
a=np.array([(10),(20),(30)], dtype=dt)
print("array is:", a)

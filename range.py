# -*- coding: utf-8 -*-
"""
Created on Wed May 18 11:44:54 2022

@author: Riaz
"""

import numpy
n= numpy.random.randint(5,30,20)
print(n)
result = numpy.max(n)-numpy.min(n)

print('result is : ',result)
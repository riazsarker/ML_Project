# -*- coding: utf-8 -*-
"""
Created on Wed May 18 11:56:12 2022

@author: Riaz
"""

import numpy as np

dataset=[8,9,2,10,3,5,7,12,15]

Q1 = np.percentile(dataset,25)

print('Q1 =',Q1)
Q2 = np.percentile(dataset,50)

print('Q2 =',Q2)
Q3 = np.percentile(dataset,75)

print('Q3 =',Q3)

IQR =Q3-Q1
print('IQR=',IQR)
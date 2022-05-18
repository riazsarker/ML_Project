# -*- coding: utf-8 -*-
"""
Created on Wed May 18 11:23:07 2022

@author: Riaz
"""

import numpy
import statistics

dataset01=[1,2,3,4,5,7,9]
#mean
mean1=numpy.mean(dataset01)
print('Mean using numpy=',mean1)
mean2=statistics.mean(dataset01)
print('Mean using Statistics',mean2)

#median
median1=numpy.median(dataset01)
print("Median using numpy",median1)
median2=statistics.median(dataset01)
print('Median using statistics',median2)

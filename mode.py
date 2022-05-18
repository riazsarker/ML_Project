# -*- coding: utf-8 -*-
"""
Created on Wed May 18 11:34:48 2022

@author: Riaz
"""

import scipy.stats
import statistics
#mode
dataset=[1,2,3,4,54,45,4,56,6,543,4,4,4,556]

mode1=statistics.mode(dataset)
print("mode using statistics=",mode1)

#mode using scipy
mode2=scipy.stats.mode(dataset)
print('mode using scipy=',mode2)
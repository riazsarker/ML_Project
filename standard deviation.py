# -*- coding: utf-8 -*-
"""
Created on Wed May 18 12:16:51 2022

@author: Riaz
"""

import numpy as np
 
population_std = np.random.randn(30)

print(population_std)

sample_std=np.random.choice(population_std,15)
print(sample_std)


result_std = np.std(population_std)
result_sample = np.std(sample_std)

print('Standard Deviation for Population',result_std)
print("Standard Deviation for sample",result_sample)
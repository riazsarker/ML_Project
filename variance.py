# -*- coding: utf-8 -*-
"""
Created on Wed May 18 12:04:15 2022

@author: Riaz
"""
import numpy as np
population=np.random.randn(30)
print(population)

sample = np.random.choice(population,20)
print(sample)

result_population=np.var(population)
result_sample=np.var(sample)

print('Result for population  : ',result_population)
print("Result for sample : ",result_sample)

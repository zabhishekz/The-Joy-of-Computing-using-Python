# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 22:58:38 2021

@author: Abhishek
"""

import numpy as np

x = np.array([1,2])
print(x.dtype)

x = np.array([1.0,2.0])
print(x.dtype)

x = np.array([1,2], dtype=np.int64)
print(x.dtype)

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

print(x+y) #element wise addition
print(np.add(x,y)) #element wise addition

print(x-y) #element wise subtraction
print(np.subtract(x,y)) #element wise subtraction

print(x*y) #element wise multiplication
print(np.multiply(x,y)) #element wise multiplication

print(x/y) #element wise division
print(np.divide(x,y)) #element wise division

print(np.sqrt(x))
print(np.sqrt(y))

print(x.T) #Transpose

print(np.sum(x)) #sum of all elements
print(np.sum(x,axis=0)) #sum of all elements column wise
print(np.sum(x,axis=1)) #sum of all elements row wise
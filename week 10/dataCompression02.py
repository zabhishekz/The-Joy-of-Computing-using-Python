# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 22:47:30 2021

@author: Abhishek
"""

import numpy as np

a = np.array([1,2,3])
print(a)
print(type(a))
print(a.shape)
print(a[0],a[1],a[2])
a[1]=6
print(a[0],a[1],a[2])

b = np.array([[1,2,3],[4,5,6]])
print(b.shape)

c = np.zeros((2,2))
print(c)

d = np.ones((2,2))
print(d)

e = np.full((2,2),6)
print(e)

f = np.random.random((2,2))
print(f)
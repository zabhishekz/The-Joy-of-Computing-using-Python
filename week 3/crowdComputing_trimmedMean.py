# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 23:00:22 2021

@author: Abhishek
"""

#below list should have 75 values but i haven't written them. Only logic
from statistics import mean
estimates = [1000, 1010, 1786, 1000, 500, 400, 120, 345, 780, 506]
estimates.sort()
tv = int(0.1*len(estimates))
estimates = estimates[tv:]
estimates = estimates[:len(estimates)-tv]
print(mean(estimates))

#shorter way to do same thing
from statistics import mean
from scipy import stats
estimates = [1000, 1010, 1786, 1000, 500, 400, 120, 345, 780, 506]
estimates.sort()
m = stats.trim_mean(estimates, 0.1)
print(m)


import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.ylabel("some values")

#'ro' red dots
#'g^' green triangles
#'r--' red dashed line
#'bs' blue square

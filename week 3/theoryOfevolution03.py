# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 23:25:11 2021

@author: Abhishek
"""

import random

print(random.randint(1,5)) #1,2,3,4,5
print(random.randrange(1,5)) #1,2,3,4
print(random.randrange(1,10,2)) #1,3,5,7,9
print(random.randrange(2,11,2)) #2,4,6,8,10
print(random.random()) #decimal number from 0 to 1
print(random.choice([1,2,3,4]))
myList=[11,45,67,89]
print(random.choice(myList))

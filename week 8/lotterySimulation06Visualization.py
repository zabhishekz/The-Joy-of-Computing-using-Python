# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 18:10:06 2021

@author: Abhishek
"""

import random
import matplotlib.pyplot as plt

#visualizing the lottery simulation problem
account=0
x=[]
y=[]

#playing game for a year
for i in range(365):
    x.append(i+1)
    
    bet=random.randint(1,10)
    lucky_draw=random.randint(1,10)
    
    if(bet==lucky_draw):
        account += 900-100
    else:
        account -= 100
    y.append(account)
print("Amount in your game account is ",account)
plt.plot(x,y)
plt.show()
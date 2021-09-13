# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 17:54:18 2021

@author: Abhishek
"""

import random

bet=int(input("Your bet from 1 to 10: "))
lucky_draw=random.randint(1,10)
print("lucky draw number is ",lucky_draw)
account=0
if(bet==lucky_draw):
    account += 900-100
else:
    account -= 100
print(account)

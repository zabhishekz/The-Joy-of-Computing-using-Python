# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 18:03:38 2021

@author: Abhishek
"""

import random
account=0
#playing game for a month
for i in range(30):
    bet=random.randint(1,10)
    lucky_draw=random.randint(1,10)
    print("Your bet number is ",bet)
    print("lucky draw number is ",lucky_draw)
    
    if(bet==lucky_draw):
        account += 900-100
    else:
        account -= 100
    print("Amount in your game account is ",account)

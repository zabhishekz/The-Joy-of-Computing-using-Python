# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 17:41:25 2021

@author: Abhishek
"""

#Tuples-immutable
ice_cream_flavours=("vanilla","chocolate","butterscoth","strawberry")
print(ice_cream_flavours)

for flavour in ice_cream_flavours:
    print(flavour)
    
print(ice_cream_flavours[2])

del ice_cream_flavours


toy=(1,2,3,4)
print(len(toy))
print(toy.count(2))

toy=(1,2,3,4,1,2,3,4,5)
print(len(toy))
print(toy.count(2))
print(toy.count(4))
print(toy.index(5))
print(toy.index(2))


rgb=("red","green","blue")
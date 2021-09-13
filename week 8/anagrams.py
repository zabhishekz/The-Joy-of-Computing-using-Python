# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 23:35:03 2021

@author: Abhishek
"""

x=[4,3,1,2]
print(sorted(x))
print(sorted(x,reverse=True))

x=['q','w','e','r','t','y']
print(sorted(x))

x="python"
print(sorted(x))

x={'q':1,'w':2,'e':4,'t':0} #sorted on base of keys
print(sorted(x))

l=["ccccc","bb","a","ddd"]
print(sorted(l,key=len))
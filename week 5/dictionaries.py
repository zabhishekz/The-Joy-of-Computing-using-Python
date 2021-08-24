# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 16:28:23 2021

@author: Abhishek
"""

conv_factor = {} #empty dictionary
conv_factor["dollar"] = 60
conv_factor["euro"] = 80
print(conv_factor)
print(conv_factor["euro"])
print(conv_factor.keys())
print(conv_factor.values())
print(conv_factor.items())
conv_factor["dollar"] = 60 #update

conv_factor["yen"] = 50
print(conv_factor)
del conv_factor["yen"]
print(conv_factor)

e=30
r=e*conv_factor["euro"]
print(r)
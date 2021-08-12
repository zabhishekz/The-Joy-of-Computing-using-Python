# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 22:52:27 2021

@author: Abhishek
"""

for i in range(1,51):
    if(i%3==0 and i%5==0):
        print(str(i)+"= fizzbuzz")
    else:
        if(i%3 == 0):
            print(str(i)+"= fizz")
        else:
            if(i%5 == 0):
                print(str(i)+"= buzz")
            else:
                print(str(i))
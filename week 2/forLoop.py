# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 19:27:44 2021

@author: Abhishek
"""

#Loops

#range(n) take values from 0 to n-1
for i in range(10):
    print("Hello", i)
    
#range(start, stop, step)
x = range(3, 6)
for n in x:
  print(n)

x = range(3, 20, 2)
for n in x:
  print(n)

    
#sum of numbers
answer = 0
for i in range(21):
    answer += i
    print("First", i,"numbers when added, gives", answer)
print("sum i ", answer)
    

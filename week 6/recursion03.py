# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 21:59:16 2021

@author: Abhishek
"""

#iterative approach
def factorial(n):
    product=1
    for i in range(1,n+1):
        product *= i
    return product

n=int(input("Enter a positive number: "))
if n<0:
    print("Factorial is not defined on negative numbers")
else:
    f=factorial(n) 
    print("Factorial of ",n," is ",f)
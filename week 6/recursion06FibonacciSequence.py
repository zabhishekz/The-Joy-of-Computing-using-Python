# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 10:26:41 2021

@author: Abhishek
"""
"""
Fibonacci Sequence:
    0th fib no = 0
    1st fib no = 1
    --------------
    2nd fib no = 1
    3rd fib no = 2
    4th fib no = 3
    5th fib no = 5
"""

def fibonacci(n):
    if(n<2):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
n=int(input("Enter a non-negative number: "))
if(n<0):
    print("Invalid input. Fibonacci udefined for negative number")
else:
    print("Fibonacci number at position", n, " is ", fibonacci(n))
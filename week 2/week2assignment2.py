# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 19:40:01 2021

@author: Abhishek
"""
#Week 2 Assignment 2: Codes

#Q-1
c = input("Enter a number: ")
print(c*5)

#Q-2
print("Hello")
print('Hello')
print(" 'Hello' ")

#Error statement 
#print(" "Hello" ")

#Q-3
for i in range(3, 30, 3):
    print(i)
    
#Q-4
c = 30
a = 4
print(c/a)
print(c//a)

#Q-5
b = 5
c = b**3
print(c)

#Q-7
c = input()
print(type(c))


#Q-10
a = 3
b = 4
c = a > b
print(c)

#Programming Assignment 1 - Hello World!
name = input()
print("Hello", name,"! Welcome to JOCP",end="")

#Programming Assignment 2 - Square of a number 
num = int(input())
print(num**2,end="")

#Programming Assignment 3 - Discount
mrp = int(input())
price = (85/100)*mrp
print(price, end="")

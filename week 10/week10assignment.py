# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 19:06:52 2021

@author: Abhishek
"""

#Week 10 : Programming Assignment 1 - String Decomposition
s=input()
a=input().split()
b=""
for i in a:
    b += i
if(set(s)==set(b) and len(s)==len(b)):
    print("Yes",end="")
else:
    print("No",end="")

#Week 10 : Programming Assignment 2 - Encryption
m=input()
n=input()
s=""
for i in range(65,91):
    s += chr(i)
ans=""
for i in m:
    c = s.index(i)
    cj = (c+5)%26
    ans += s[cj]
if(sorted(n)==sorted(ans)):
    print("Yes",end="")
else:
    print("No",end="")
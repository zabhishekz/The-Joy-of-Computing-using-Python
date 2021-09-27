# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 22:11:23 2021

@author: Abhishek
"""

#Week 9: Programming Assignment 1 - Snakes and Ladders I
con=input().split(",")
d={}
s=0
l=0
for c in con:
    k=c.split(":")
    d[int(k[0])]=int(k[1])
for key in d:
    if key>d[key]:
        s += 1
    else:
        l +=1 
print(s,l,end="")


#Week 9: Programming Assignment 2 - Snakes and Ladders II
con=input().split(",")
throw=input().split(",")
d={}
for c in con:
    y=c.split(":")
    d[int(y[0])]=int(y[1])
p=0
for t in throw:
    p += int(t)
    if p in d.keys():
        p=d[p]
if p>99:
    print("Yes",end="")
else:
    print("No",end="")

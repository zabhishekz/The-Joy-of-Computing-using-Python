# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 21:46:44 2021

@author: Abhishek
"""
a=[1,2,3,4,5,6,7,8,9,10]
for i in range(0,len(a),2):
    print(a[i])
    
a=[1,2,3,4,5,6,7,8,9,10]
a.insert(-3,999)
print(a)

shopping=["bread","cake","muffins"]
shopping.insert(len(shopping),"oil")
print(shopping)

a="Hello"
print("+".join(a))

#programming aassignment 1
s = input()
l = s.split()
a = int(l[0])
b = int(l[1])
print(a*b, end="")

#programming aassignment 2
s = input()
l = s.split()
print(abs(int(max(l))-int(min(l))),end="")

#programming aassignment 3
s = list(map(int,input().split()))
bh = [a for a in s if a!=max(s)]
if(max(s)**2 == (bh[0]**2+bh[1]**2)):
    print("YES",end="")
else:
    print("NO",end="")
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 12:37:13 2021

@author: Abhishek
"""

#Week 12: Programming Assignment 1 - Candies
l = list(map(int,input().split()))
m = 0
total = sum(l)
if total%len(l)!=0:
    print('-1',end='')
else:
    avg = total//len(l)
    for i in l:
        if i > avg:
            m += (i-avg)
    print(m,end="")
    
#Week12: Programming Assignment 2 - Suitcases
sb = list()
for a in (input().split()):
    sb.append(int(a))
sb.sort()
print(sb[-1]+sb[-2],end="")


#Week12: Programming Assignment 3 - Game of Strengths
for t in range(int(input())):
    n = int(input())
    a = [int(i1) for i1 in input().split()]
    mn,mnidx,mx,mxidx=a[0],0,a[0],0
    for i in range(0,n):
        if a[i]<mn:
            mn=a[i]
            mnidx=i
        if a[i]>mx:
            mx=a[i]
            mxidx=i
    val1 = max(mnidx,mxidx)
    val2 = min(mnidx,mxidx)
    print(min([val2-val1+1+n,val1+1,n-val2]))

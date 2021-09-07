# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 20:22:36 2021

@author: Abhishek
"""
#Week 7: Programming Assignment 1 - Binary Matrix
l=list(map(int,input().split()))
m=l[0]
n=l[1]
a=[]
for i in range(m):
    r=list(map(int,input().split()))
    a.append(r)

f=1
for i in range(m):
    for j in range(n):
        if(a[i][j]!=1 and a[i][j]!=0):
            f=0
            break
        if(f==0):
            break
if(f==1):
    print("Yes",end="")
else:
    print("No",end="")


#Week 7: Programming Assignment 2 - Number Triangle II
n=int(input())
for i in range(1,n+1):
    for k in range(1,i+1):
        print(k,end="")
    for m in range(i-1,0,-1):
        print(m,end="")
    if(i==n):
        print(end="")
        break
    print()
            

#Week7: Programming Assignment 3 - Lower Triangular Matrix
n=int(input())
a=[]
for i in range(n):
    l=list(map(int,input().split()))
    a.append(l)

for i in range(n):
    for j in range(n):
        if(j>i):
            a[i][j]=0

for i in range(n):
    for j in range(n):
        if(i== n-1 and j == n-1):
            print(a[i][j],end="")
        elif(j==n-1 and i != n-1):
            print(a[i][j])
        else:
            print(a[i][j],end=" ")
    
    
            
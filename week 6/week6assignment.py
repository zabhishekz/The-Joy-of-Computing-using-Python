# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 16:56:08 2021

@author: Abhishek
"""
import string
s="hello"
n=""
for i in range(len(s)):
    c=int(ord(s[i])-26)
    n += chr(c)
print(n)


s="hello, and welcome to the joy of computing"
if(s.capitalize()==s[0:1].upper()+s[1:len(s)]):
    print("true")
else:
    print("false")
    
print(s[::2].replace("e","l"))

#Week 6: Programming Assignment 1 - Matrix
l=list(map(int,input().split()))
r=l[0]
c=l[1]
k=1
for i in range(1,r+1):
    for j in range(1,c+1):
        if(j != c):
            print(k,"",end="")
        else:
            print(k,end="")
        k+=1
    if(i!=r):
        print("")
    else:
        print("",end="")
    
        
#Week 6: Programming Assignment 2 - Number Triangle I
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    if(i!=n):
        print("")
    print("",end="")

#Week 6: Programming Assignment 3 - Symmetric Matrix
n=int(input())
mat=[]
f=0
for i in range(n):
    mat.append(input().split())
for a in range(len(mat)):
    for b in range(n):
        if mat[a][b] != mat[b][a]:
            f=1
if f==0:
    print("Yes",end="")
else:
    print("No",end="")

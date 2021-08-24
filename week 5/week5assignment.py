# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 17:29:20 2021

@author: Abhishek
"""

dict1={"ID":"0121","Name":"zzz"}
dict2={"Name":"zzz"}
dict2.update({"ID":"0121"})
if(dict1==dict2):
    print("They are equal")
else:
    print("They are not equal")
    
dictA={"name":"Joy of computing",
       "Length":"12 weeks",
       "Professor_name":"Dr Sudarshan Iyengar",
       "Language":"Python"}
dictB={}
dictB.update(dictA)
for x,y in dictB.items():
    print(x,y)
    
import random
a=[1,2,3,4,5,6]
sum=0
for i in range(0,2):
    sum += random.choice(a)
print(sum)

l=[]*100
for i in range(100):
    l.append(i+1)
flag=0
k=108
for i in range(100):
    if(k==l[i]):
        print("Element is present at position ",i)
        flag=1
        break
if(flag==0):
    print("element is not present in given list")


a=["1","2","3","4","5"]
fun=len
print(fun(a))

#Week 5: Programming Assignment 1 - k times
l = list(input().split())
k = int(input())
dict={}
for i in l:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

for i in dict:
    v = dict[i]
    v = int(v)
    if(v == k):
        print(i,end="")
        break

#Week 5: Programming Assignment 2 - kth Largest
def bubble_sort(a):
    n = len(a)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if(a[j]>a[j+1]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp

a = list(map(int,input().split()))
k = int(input())
bubble_sort(a)
print(a[k-1],end="")

#Week 5: Programming Assignment 3 - Cumulative sum
a = list(map(int,input().split()))
n = len(a)
j=a[0]
cs = []
cs.append(a[0])
for i in range(1,n):
    j += a[i]
    cs.append(j)
    
print(*cs,end="")
    
         
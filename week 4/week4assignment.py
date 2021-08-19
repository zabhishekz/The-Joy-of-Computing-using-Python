# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 19:44:09 2021

@author: Abhishek
"""
#week 4 quiz
l=[31,0,31,30,31,30,31,31,30,31,30,31]
a=1900
if(a%4==0 and a%100!=0 or a%400==0):
    l.insert(1, 29)
else:
    l.insert(1, 28)
print("In the year 1900, february has",l[1], "days")


import datetime
x=datetime.datetime.now()
print(x.strftime("%W"))
print(x.strftime("%w"))

a=input("Enter any positive number\n")
p=int(a)
sum=0
while(p!=0):
    sum = sum +p%10
    p //= 10

print(sum)


import random
l=["abc","cde","efg","hij"]
a=random.choice(l)
print("".join(random.sample(a,len(a))))


a=0
b=1
print(a,end="")
for i in range(0,15,1):
    print(b,end=" ")
    a,b=b,a+b


#Week 4: Programming Assignment 1 - Factorial
n = int(input())
f=1
for i in range(1,n+1):
    f *= i
print(f,end=" ")
 

#Week 4: Programming Assignment 2 - Multiples
s = list(map(int,input().split()))
count = 0
for num in s:
    if(num%3 == 0 or num%5 == 0):
        count += 1
print(count,end="")

#Week 4: Programming Assignment 2 - Multiples
n = input().split()
c = 0
for a in n:
    if( int(a)%5==0 or int(a)%3==0):
        c += 1
print(c,end="")


#Week 4: Programming Assignment 3 - Arrangements
import math
n = input().split()
ans = math.factorial(len(n))//(math.factorial(n.count('1'))*math.factorial(n.count('0')))
print(ans,end="")
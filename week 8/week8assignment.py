# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 09:40:25 2021

@author: Abhishek
"""

#Week 8: Programming Assignment 1 - Palindrome
ostr=input()
ostr=ostr.lower()
l=len(ostr)
rem=[]
for i in range(l):
    if (ord(ostr[i])>=97 and ord(ostr[i])<=122):
        continue
    else:
        rem.append(ostr[i])

for j in rem:
    f=ostr.find(j)
    ostr=ostr[:f]+ostr[f+1:]

rstr=ostr[::-1]
if(ostr==rstr):
    print("Yes",end="")
else:
    print("No",end="")
    

#Week 8: Programming Assignment 2 - Anagrams
str1=input()
str2=input()
str1=str1.lower()
str2=str2.lower()
l=len(str1)
rem=[]
for i in range(l):
    if (ord(str1[i])>=97 and ord(str1[i])<=122):
        continue
    else:
        rem.append(str1[i])

for j in rem:
    f=str1.find(j)
    str1=str1[:f]+str1[f+1:]
    
l=len(str2)
rem=[]
for i in range(l):
    if (ord(str2[i])>=97 and ord(str2[i])<=122):
        continue
    else:
        rem.append(str2[i])

for j in rem:
    f=str2.find(j)
    str2=str2[:f]+str2[f+1:]

if(sorted(str1)==sorted(str2)):
    print("Yes",end="")
else:
    print("No",end="")


#Week 8: Programming Assignment 3 - Pangram
alphabets=[]
for i in range(97,123):
    alphabets.append(chr(i))
    
str=input()
str=str.lower()
l=[]

for i in str:
    if(i != " " and i not in l):
        l.append(i)
    else:
        continue
    
l=sorted(l)
if(l==alphabets):
    print("Yes",end="")
else:
    print("No",end="")
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 18:24:07 2021

@author: Abhishek
"""

#Week 11: Programming Assignment 1 - Sorting of Words
str=input()
l=str.split(",")
l.sort()
for i in range(len(l)):
    if(i==len(l)-1):
        print(l[i],end="")
    else:
        print(l[i],end=",")


#Week 11: Programming Assignment 2 - Puncutations
punctuations='''!()-[]{}:;'"\,<>./?@#$%^&*_~'''
str=input()
for i in str:
    if i in punctuations:
        str=str.replace(i, "")
print(str,end="")


#Week 11: Programming Assignment 3 - Solve the riddle
def findLongestPalindrome(strr):
	count = [0]*256
	for i in range(len(strr)):
		count[ord(strr[i])] += 1
	beg = ""
	mid = ""
	end = ""
	ch = ord('a')
	while ch <= ord('z'):
		if (count[ch] & 1):
			mid = ch
			count[ch] -= 1
			ch -= 1
		else:
			for i in range(count[ch]//2):
				beg += chr(ch)
		ch += 1
	end = beg
	end = end[::-1]
	return beg + chr(mid) + end
n=int(input())
L=[]
for a in range(n):
      L.append(len(findLongestPalindrome(input())))
for b in L:
      print(b)


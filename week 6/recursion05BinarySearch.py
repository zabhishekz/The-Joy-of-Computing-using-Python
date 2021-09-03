# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 09:49:34 2021

@author: Abhishek
"""

def binary_search(l,x,start,end):
    #base case: 1 element in list
    if(start==end):
        if(l[start]==x):
            return start
        else:
            return -1
    else:
        #divide the array into halves
        mid=int((start+end)/2)
        if l[mid]==x:
            return mid
        elif l[mid]>x:
            return binary_search(l, x, start, mid-1)
        else:
            return binary_search(l, x, mid+1, end)
        
l=[20,45,60,70,90]
x=int(input("Enter value to search in list "))
index=binary_search(l, x, 0, len(l)-1)
if index == -1:
    print(x," not found")
else:
    print(x, "is found at position ", index+1)
        
        
    
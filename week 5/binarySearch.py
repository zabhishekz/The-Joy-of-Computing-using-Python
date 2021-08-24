# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 17:16:43 2021

@author: Abhishek
"""

def binary_search(a,x):
    first_pos = 0
    last_pos = len(a)-1
    flag=0
    count=0
    while(first_pos<=last_pos and flag==0):
        count+=1
        mid=(first_pos+last_pos)//2
        if(x==a[mid]):
            flag=1
            print("The element is present at position: "+str(mid))
            print("The number of iterations are "+str(count))
            return
        elif(x<a[mid]):
            last_pos=mid-1
        elif(x>a[mid]):
            first_pos=mid+1
        
            
    print("The number is not present")
        
a=[]
for i in range(1,1001):
    a.append(i)
    
binary_search(a, 1000)
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 19:05:25 2021

@author: Abhishek
"""
def spiral(m,n,a):
    k=0
    l=0
    '''
    k is index of starting row
    l is index of starting column
    '''
    while(k<m and l<n):
        #print 1st row
        for i in range(l,n):
            print(a[k][i], end=" ")
        k+=1
        
        #print last column
        for i in range(k,m):
            print(a[i][n-1], end=" ")
        n-=1
        
        if(k<m):
            #print last row
            for i in range(n-1, l-1, -1):
                print(a[m-1][i],end=" ")
            m -= 1
            
        if(l<n):
            #print first column
            for i in range(m-1, k-1, -1):
                print(a[i][l], end=" ")
            l += 1
        
a=[]
count=1
for i in range(4):
    l=[]
    for j in range(4):
        l.append(count)
        count += 1
    a.append(l)
    
spiral(4, 4, a)
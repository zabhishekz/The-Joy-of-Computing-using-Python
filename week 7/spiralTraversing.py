# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 19:05:25 2021

@author: Abhishek
"""
import turtle

turtle.bgcolor("black")
seurat = turtle.Turtle()
width =  5
height = 7
dot_distance = 25
seurat.setpos(-250,250)

def spiral(m,n):
    k=0
    l=0
    f=0
    seurat.color("white")
    '''
    k is index of starting row
    l is index of starting column
    '''
    while(k<m and l<n):
        if f==1:
            seurat.right(90)
            
        #print 1st row
        for i in range(l,n):
            seurat.forward(dot_distance)
            #print(a[k][i], end=" ")
        k+=1
        f=1
        
        seurat.right(90)
        #print last column
        for i in range(k,m):
            seurat.forward(dot_distance)
            #print(a[i][n-1], end=" ")
        n-=1
        seurat.right(90)
        
        if(k<m):
            #print last row
            for i in range(n-1, l-1, -1):
                seurat.forward(dot_distance)
                #print(a[m-1][i],end=" ")
            m -= 1
        seurat.right(90)
            
        if(l<n):
            #print first column
            for i in range(m-1, k-1, -1):
                seurat.forward(dot_distance)
                #print(a[i][l], end=" ")
            l += 1
        
spiral(20,20)
turtle.done()
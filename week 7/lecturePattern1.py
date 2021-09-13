# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 15:42:37 2021

@author: Abhishek
"""
import turtle
seurat = turtle.Turtle()
from random import randint

width =  5
height = 7
dot_distance = 25


seurat.color("blue")

n=4
"""
n=int(input())
l=[]
for i in range(n):
    a=list(map(int,input().split()))
    l.append(a)

print()
"""
seurat.left(180)

for i in range(n):
    if(i%2==0):
        for j in range(n-1,-1,-1):
            seurat.dot()
            seurat.forward(dot_distance)
            #print(l[i][j],end=" ")
        seurat.left(90)
        seurat.forward(dot_distance)
        seurat.left(90)
    else:
        for j in range(n):
            seurat.dot()
            seurat.forward(dot_distance)
            #print(l[i][j],end=" ")
        seurat.right(90)
        seurat.forward(dot_distance)
        seurat.right(90)
    
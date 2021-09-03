# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:29:20 2021

@author: Abhishek
"""


ar=int(input("Enter number of rows in matrix A: "))
ac=int(input("Enter number of cols in matrix A: "))
br=int(input("Enter number of rows in matrix B: "))
bc=int(input("Enter number of cols in matrix B: "))
if(ac != br):
    print("Matrix multiplication not possible")
    
    
A=[]
B=[]

print("Enter elements of matrix A: ")
for i in range(0,ar):
    A.append(list(map(int,input().split())))
    
print("Enter elements of matrix b: ")
for i in range(0,br):
    B.append(list(map(int,input().split())))
    
print(A)
print(B)
        
r=[[0]*bc]*ar
print(r)
for i in range(ar):
    for j in range(bc):
        for k in range(br):
            r[i][j] += A[i][k]*B[k][j]

print("Resultant matrix is:\n",r)
    
    
    
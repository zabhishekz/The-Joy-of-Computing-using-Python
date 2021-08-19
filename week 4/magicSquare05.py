# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 23:38:51 2021

@author: Abhishek
"""

def magic_square(n):
    
    magicSquare = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        magicSquare.append(l)
        
    i = n//2
    j = n-1
    num = n*n
    count = 1
    
    while(count <= num):
        if(i == -1 and j == n): #condition 4
            i = 0
            j = n-2
        else:
            if(j == n): #condition 2
                j = 0
                
            if(i < 0): #condition 2
                i = n-1
        
        if(magicSquare[i][j] != 0): #condition 3
            j = j-2
            i = i+1
            continue
        else:
            magicSquare[i][j] = count
            count += 1
            
        i = i-1
        j = j+1 #condition 1
        
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j], end=" ")
        print()
    print("the sum of each row/column/diagonal is: "+str(n*(n**2+1)/2))
    
magic_square(3)
magic_square(5)
magic_square(7)
        
            
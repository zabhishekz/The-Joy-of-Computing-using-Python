# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:03:18 2021

@author: Abhishek
"""

def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print( "Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
          
n=int(input("Enter the number of disks: "))
TowerOfHanoi(n,'A','B','C') 
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 12:26:44 2021

@author: Abhishek
"""

def check_num(num):
    itr=1
    
    while(num!=1):
        if(num%2==0):
            num = int(num/2)
            itr += 1
        else:
            num = num*3 + 1
            itr += 1
            
    print(num,itr)
    
check_num(256)
            
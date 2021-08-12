# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 23:14:37 2021

@author: Abhishek
"""

with open('file1.txt', "r+") as myfile:
    print(myfile.read())
    myfile.write("I am fine")
myfile.close()

#'r' read only mode
#'w' write mode 
#'a' appending mode
#'r+' special read and write mode
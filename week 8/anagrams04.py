# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 23:46:01 2021

@author: Abhishek
"""

str1=input("Enter the first string: ")
str2=input("Enter the second string: ")
if(sorted(str1)==sorted(str2)):
    print("These are anagrams")
else:
    print("These are NOT grams")
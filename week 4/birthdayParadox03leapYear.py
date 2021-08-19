# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 10:33:00 2021

@author: Abhishek
"""

"""
birthdate will be generated according to birth month
jan, march, may, july, aug, oct, dec = 31 days
april, june, sept, nov = 30 days
feb has 29 days if year is leap year and 28 if it isn't leap year

For an year to be a leap year, it must be divisible by 4 if it is not a century year 
and must be divisible by 400 if it is a century year


Algo-
if year is divisible by 400 then is leap year
else if year is divisible by 100 then not leap year
else if year is divisible by 4 then is leap year
else not leap year
"""
import random

year = random.randint(1993,2018)
print(year)
if(year%4 == 0 and year%100 != 0 or year%400 == 0):
    print("Given year is a leap year")
else:
    print("Given year is not a leap year")
    

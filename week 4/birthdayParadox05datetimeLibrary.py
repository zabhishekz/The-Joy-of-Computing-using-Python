# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 11:58:03 2021

@author: Abhishek
"""
import datetime
print(datetime.date.today())
print(datetime.date.today().strftime("%Y"))
print(datetime.date.today().strftime("%B"))
print(datetime.date.today().strftime("%d"))

print("Week number of the month",datetime.date.today().strftime("%W"))
print("Weekday of the week",datetime.date.today().strftime("%w"))
print("Day of the year",datetime.date.today().strftime("%j"))
print("Day of the week",datetime.date.today().strftime("%A"))
print("Current time",datetime.datetime.now())
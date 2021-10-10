# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 16:34:51 2021

@author: Abhishek
"""

import calendar

def check_leap(y):
    if y%100==0: #if year is century year check divisibility by 400 
        if y%400==0:
            return True
        else:
            return False
    else:
        if y%4==0: #if year is NOT a century year check divisibility by 4
            return True
        else:
            return false
        
def check_valid_date(dt,m, y, l):
    if(l==True):
        if(m==2):
            if dt<30:
                return True
            else:
                return False
        else:
            if m<8:
                if(m%2==1):
                    if dt<32:
                        return True
                    else:
                        return False
                else:
                    if(dt<31):
                        return True
                    else:
                        return False
            else:
                if(m%2==0):
                    if dt<32:
                        return True
                    else:
                        return False
                else:
                    if(dt<31):
                        return True
                    else:
                        return False
    else:
        if(m==2):
                if dt<29:
                    return True
                else:
                    return False
        else:
            if m<8:
                if(m%2==1):
                    if dt<32:
                        return True
                    else:
                        return False
                else:
                    if(dt<31):
                        return True
                    else:
                        return False
            else:
                if(m%2==0):
                    if dt<32:
                        return True
                    else:
                        return False
                else:
                    if(dt<31):
                        return True
                    else:
                        return False
        

def get_day(day_index):
    list_of_days=["Monday", "tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return list_of_days[day_index]
        
while(1):
    year=int(input("Enter a year(1970-2021): "))
    if(year<1970):
        print("Entear valid year in the range(1970-2021): ")
    else:
        break
    
while(1):
    month=int(input("Enter a month(1-12): "))
    if(month<=12 and month>=1):
        break
    else:
        print("Entear valid month in the range(1-12): ")
        
leap=check_leap(year)

while(1):
    date=int(input("Enter a date: "))
    if date>0 and check_valid_date(date,month,year,leap):
        break
    else:
        print("Entear a valid date: ")
        
day_index=calendar.weekday(year, month, date)
day=get_day(day_index)
print(date,"/",month,"/",year," falls on ",day)

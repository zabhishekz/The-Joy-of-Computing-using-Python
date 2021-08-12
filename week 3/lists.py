# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 22:37:02 2021

@author: Abhishek
"""

#list
shopping=["bread", "coffee", "sugar"]
print(shopping)

for item in shopping:
    print(item)
    
#append
shopping.append("Curd")
shopping.append("Shampoo")
print(shopping)

#insert
shopping.insert(1,"Oil")
print(shopping)

#count
ages=[12,23,42,34,15,87,12,16,25,23,82,57,7,3,2, 3,1,20]
print(ages.count(25))
print(ages.count(12))
print(ages.count(70))

#len
print(len(ages))
print(len(shopping))

for i in range(len(shopping)):
    print(shopping[i])

#sort
ages.sort()
print(ages)

#reverse
ages.reverse()
print(ages)

students=["Arun","Rajesh","Harish","akansha","lakshmi","varshha"]
students.sort()
print(students)
students.insert(0,"JOC")
print(students)

#slicing
#list_name[start_index:len(list_name)]
print(students[1:5])
print(students[:])
print(students[3:])
print(students[:5])
print(students[2:5])


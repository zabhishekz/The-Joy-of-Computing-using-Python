# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 11:12:14 2021

@author: Abhishek
"""

#q1- Write a Python script to sort (ascending and descending) a dictionary by value.
import operator
dict={"v": 5, "y": 2, "m": 3, "a": 6}
print('Original dictionary : ',dict)
sorted_dict = sorted(dict.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_dict)
sorted_dict = sorted(dict.items(), key=operator.itemgetter(1),reverse=True)
print('Dictionary in descending order by value : ',sorted_dict)


#q2- Write a Python script to add a key to a dictionary.
dict1={0: 10, 1: 20}
dict1[2] = 30
print(dict1)


#q3- Write a Python script to concatenate following dictionaries to create a new one.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
sample = {}
for i,j in dic1.items():
    sample.update({i:j})
for i,j in dic2.items():
    sample.update({i:j})
for i,j in dic3.items():
    sample.update({i:j})
print(sample)




#q4- Write a Python script to check whether a given key already exists in a dictionary.
q4={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
n=int(input("Enter integer key to check if it is present in q4 dict: "))
x=q4.get(n,0)
if(x!=0):
    print("Present")
else:
    print("Not Present")
    
    
#q5- Write a Python program to iterate over dictionaries using for loops.
q5={1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F"}
for key in q5:
    print(key, q5[key], end= " ")
   
    
#q6- Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
n=int(input("Enter a number to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x): "))
q6={}
for i in range(1,n+1):
    q6.update({i:i*i})
print(q6)


#q7- Write a Python script to merge two Python dictionaries
q7a = {'a': 1, 'b': 2}
q7b = {'c': 3, 'd' : 4}
q7a.update(q7b)
print(q7a)


#q8- Write a Python program to get the maximum and minimum value in a dictionary.
q8 = {'x':76, 'y':23, 'z': 54}
val_max = max(q8.values())
val_min = min(q8.values())
print('Maximum Value: ',val_max)
print('Minimum Value: ',val_min)


#q9- Write a Python program to get a dictionary from an object's fields.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
q9=d1
for el in d2:
    if el not in q9:
        q9[el]=d2[el]
    else:
        q9[el]=q9[el]+d2[el]
print(q9)


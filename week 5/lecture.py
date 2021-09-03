# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 15:25:35 2021

@author: Abhishek
"""
#ques1

import random

quotes = [
    "You’re off to great places, today is your day. Your mountain is waiting, so get onyour way.",
    "You always pass failure on the way to success.",
    "No one is perfect - that’s why pencils have erasers.",
    "Winning doesn’t always mean being first. Winning means you’re doing better than you’ve done before.",
    "You’re braver than you believe, and stronger than you seem, and smarter than you think.",
    "It always seems impossible until it is done.",
    "Keep your face to the sunshine and you cannot see a shadow.",
    "Once you replace negative thoughts with positive ones, you’ll start having positive results.",
    "Positive thinking will let you do everything better than negative thinking will.",
    "In every day, there are 1,440 minutes. That means we have 1,440 daily opportunities to make a positive impact.",
    "The only time you fail is when you fall down and stay down.",
    "When you are enthusiastic about what you do, you feel this positive energy. It’s very simple.",
    "Positive anything is better than negative nothing."
    ]

print("The quote of the day is: \n",random.choice(quotes))



#ques2
nums=[]
for i in range(1,49):
    nums.append(i)

for i in range(0,7):
    print(random.choice())

#ques3
list=[]
for i in range(5):
    n = input()
    list.append(n)
s="+".join(list)
print(s)

#ques4a
s=input("Enter a sentence: ")
l=s.split()
print(l[2])

#ques4b
s=input("Enter a sentence: ")
l=s.split()
n=len(l)
for i in range(n):
    j=i+1
    if(j%3==0):
        print(l[i])
        
        
#ques5a
s=input("Enter a sentence: ")
l=s.split()
random.shuffle(l)
str=" ".join(l)
print(str)

#ques5b
s=input("Enter a sentence: ")
l=s.split()
l[0]=l[0].lower()
random.shuffle(l)
l[0]=l[0].capitalize()
str=" ".join(l)
print(str)
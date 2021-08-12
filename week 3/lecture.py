# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 23:15:52 2021

@author: Abhishek
"""

#create list
words=['rainbow','computer', 'science', 'programming', 'mathematics', 'player']

#traverse- first method
print(words)

#traverse- second method
for word in words:
    print(word)
    
print("\n")
    
#traverse- third method
for i in range(len(words)):
    print(words[i])
    
#sort
words.sort()
ages=[12,23,42,34,15,87,1]
ages.sort()
print("\nwords List after sorting: ", words)
print("\nages List after sorting: ",ages)

    
#insert
words.insert(0, "apple")
print("\nwords List after insert: ", words)

#slicing
print("\nslicing operations")
print(words[1:5])
print(words[:])
print(words[3:])
print(words[:5])

#append
words.append("book")
print("\nwords List after append: ", words)

#remove
words.remove("science")
print("\nwords List after remove: ", words)

#pop
words.pop(2)
print("\nwords List after pop: ", words)

new_words=["cloud","data","library"]
words.extend(new_words)

print("\nwords List after extend: ", words)

#clear
ages.clear()
print("\nages List after clear: ", ages)

#index
print("\nIndex of word player in list: ",words.index("player"))

#count
print("\nnumber of occurrences of word computer",words.count("player"))

#reverse
print("\nwords List before reverse: ",words)
words.reverse()
print("\nwords List after reverse: ", words)

#copy
duplicate_words = words.copy()
print("\nduplicate_words list: ",duplicate_words)

#sum
nums = [3, 5, 1, 7, 9, 11]
print("\nsum of numbers: ",sum(nums))

#max
print("\nmax of numbers: ",max(nums))

#min
print("\nmin of numbers: ",min(nums))

#ord
for n in nums:
    print(ord(n))
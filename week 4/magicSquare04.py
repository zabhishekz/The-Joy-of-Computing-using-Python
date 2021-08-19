# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 20:22:53 2021

@author: Abhishek
"""

"""
fact-
m = n(n^2+1)/2

steps-
1) 1 is located at position (n/2,n-1)
2) let's say position of 1 is (p,q), then next number which is 2 is located at (p-1,q+1) position.
Anytime if the calculated row position becomes -1 then make it n-1 or column position becomes n then make it 0
3) if the calculated position already contains a number then decrement the column by 2 and increment row by 1
4) if anytime row position becomes -1 AND column becomes n, switch it to (0,n-2)

example-
n=3
1) position of 1: = (3/2,3-1) = (1,2)    ...(p,q)
2) position of 2: = (p-1, q+1) = (1-1,2+1) = (0,3) = (0,0)   ...(p,q)
3) position of 3: = (p-1, q+1) = (0-1,0+1) = (-1,1) = (3-1, 1) = (2,1)
4) position of 4: = (2-1,1+1) = (1,2)
    Since 1 is already present at this position, apply 2nd condition = (1+1,2-2) = (2,0)
5) position of 5: = (2-1,0+1) = (1,1)
6) position of 6: = (1-1,1+1) = (0,2)
7) position of 7: = (0-1,2+1) = (-1,3)
    condition 3: (0,1)
8) position of 8: = (0-1,1+1) = (-1,2) = (2,2)
9) position of 9: = (2-1, 2+1) = (1,3) = (1,3) = (1,0)
"""

#matrix using lists
def magic_square(n):
    magicSquare = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        magicSquare.append(l)
        
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j], end=" ")
        print()
        
magic_square(3)



#loop inside list 
magic = [0 for i in range(3)]
print(magic)

#loops inside list
magic = [[0 for i in range(3)] for j in range(3)]
print(magic)

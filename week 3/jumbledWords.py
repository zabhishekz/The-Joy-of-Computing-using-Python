# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 23:08:04 2021

@author: Abhishek
"""

import random

def choose():
    words=['rainabow','computer', 'science', 'programming', 'mathematics', 'player', 'condition', 'reverse', 'water', 'board']
    pick = random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thank(p1n, p2n, p1, p2):
    print(p1n, "Your socre is: ",p1)
    print(p2n, "Your socre is: ",p2)
    print("Thanks for playing")

def play():
    p1name = input("Player 1, Please enter your name")
    p2name = input("Player 2, Please enter your name")
    pp1 = 0
    pp2 = 0
    turn = 0
    while(1):
        #computer's task
        picked_word = choose()
        #create question
        qn=jumble(picked_word)
        print(qn)
        #for player 1
        if (turn%2 == 0):
            print(p1name,"Your turn. ")
            ans = input("What is on my mind? ")
            if ans == picked_word:
                pp1 += 1
                print("Your score is: ",pp1)
            else:
                print("Better luck next time. I thought :", picked_word)
            c=int(input("Press 1 to continue, 0 to quit"))
            if(c==0):
                thank(p1name,p2name,pp1, pp2)
                break
        #for player 2
        else:
            print(p2name,"Your turn. ")
            ans = input("What is on my mind? ")
            if ans == picked_word:
                pp2 += 1
                print("Your score is: ",pp2)
            else:
                print("Better luck next time. I thought :", picked_word)
            c=int(input("Press 1 to continue, 0 to quit"))
            if(c==0):
                thank(p1name,p2name,pp1, pp2)
                break
        turn += 1
    
play()
        
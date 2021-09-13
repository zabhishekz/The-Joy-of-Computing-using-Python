# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 23:21:28 2021

@author: Abhishek
"""

#Flipping the image


from PIL import Image

#opening the image
img=Image.open("obtained.png")

#transposing
transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT)

#save it to a file in  a human understandable format
transposed_img.save("corrected.png")

print("Done flipping")



 
#Image enhancement CLAHE


import cv2

#Read the image
img=cv2.imread("crime.png")

#Preparation for CLAHE
clahe=cv2.CreateCLAHE()

#Convert ot gray scale image
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Apply enhancement
enh_img=clahe.apply(gray_img)

#save it to a a file
cv2.imwrite("enhanced.png",enh_img)

print("Done enhancing")

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:51:21 2021

@author: Abhishek
"""

from PIL import Image

im=Image.open('test1.png')
rgb_im=im.convert('RGB')
r,g,b=rgb_im.getpixel((1,1))
print(r,g,b)
r,g,b=rgb_im.getpixel((150,1))
print(r,g,b)
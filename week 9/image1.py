# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:09:47 2021

@author: Abhishek
"""

import numpy as np
from PIL import Image

width=5
height=4
array=np.zeros([height,width,3],dtype=np.uint8)
img=Image.fromarray(array)
img.save('test.png')
array1=np.zeros([100,200,3],dtype=np.uint8)
array1[:,:100]=[255,128,0]#orange
array1[:,100:]=[0,0,255]#blue
img=Image.fromarray(array1)
img.save('test1.png')
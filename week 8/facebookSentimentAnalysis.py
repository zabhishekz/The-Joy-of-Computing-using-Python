# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 23:50:05 2021

@author: Abhishek
"""

import pandas as pd
import nltk 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download("vader_lexicon")
file="/Users/Abhishek/Downloads/data_file1.xlsx"
xl=pd.ExcelFile(file) #Read from Excel file
dfs=xl.parse(xl.sheet_names[0]) #Parsing excel sheet to data frame
dfs=list(dfs['Timeline'])#removes blank rows from data frames
print(dfs)

sid=SentimentIntensityAnalyzer()
str1="UTC+05:30"
for data in dfs:
    a=data.find(str1)
    if(a==-1):
        ss=sid.polarity_scores(data)
        print(data)
        for k in ss:
            print(k,ss[k])

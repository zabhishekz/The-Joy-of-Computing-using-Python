# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 16:12:44 2021

@author: Abhishek
"""

from selenium import webdriver
browser=webdriver.Chrome(r"C:\Users\Abhishek\Downloads\chromedriver.exe")

browser.get("https://www.seleniumhq.org")

elem=browser.find_element_by_link_text("Downloads")
elem.click()

search=browser.find_element_by_id('q')
search.send_keys('Downloads')
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 20:24:00 2021

@author: Abhishek
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(r"C:\Users\Abhishek\Downloads\chromedriver.exe")
driver.get("https://web.whatsapp.com/")
wait=WebDriverWait(driver, 600)

target='"Manav"'#friend's name
string="Message sent using python"#message
x_arg='//span[contains(@title, '+ target + ')]'
target=wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
target.click()

input_box=driver.find_element_by_class_name("_13NKt")
for i in range(10):
    input_box.send_keys(string+Keys.ENTER)


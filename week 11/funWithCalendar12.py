# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 17:02:02 2021

@author: Abhishek
"""

from datetime import datetime as dt
import pytz

timezones=pytz.all_timezones

for i in range(len(timezones)):
    zone=timezones[i]
    tz=pytz.timezone(zone)
    print("Current time at zone ", zone, " is ", dt.now(tz))
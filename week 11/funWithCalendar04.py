# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 16:18:19 2021

@author: Abhishek
"""

from datetime import datetime as dt

#current time
print(dt.now())

import pytz

tz=pytz.timezone("Singapore")
print(dt.now(tz))

print(pytz.all_timezones)
print(len(pytz.all_timezones))

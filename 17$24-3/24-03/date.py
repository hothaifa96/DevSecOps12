# ts = 1679649830
#
# ts = ts / 60
# ts = ts / 60 # hours
# ts = ts / 24 # days
# ts = ts / 365 # years
#
# print(ts)

import datetime
#
# x = datetime.datetime.now()
# print(x)
# print(x.year)
# print(x.month)
# print(x.day)
# print(x.hour)
# print(x.minute)
#
# print(f'{x.day}/{x.month}/{x.year}')
# print(f'{x.day}-{x.month}-{x.year}')
import time
import requests

start = time.time_ns()
time.sleep(10)
end = time.time_ns()

total_app_time = (end-start) / (10**9)
print(total_app_time)
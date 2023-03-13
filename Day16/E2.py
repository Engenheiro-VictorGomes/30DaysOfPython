# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
from datetime import datetime

# Solution 01
now = datetime.now()
day = now.day                   # 8
month = now.month               # 7
year = now.year                 # 2021
hour = now.hour                 # 7
minute = now.minute             # 38
second = now.second
print(f'{month}/{day}/{year}, {hour}:{minute}:{second}')

# Solution 02

now = datetime.now()
print(now.strftime("%m/%d/%Y %H:%M:%S"))

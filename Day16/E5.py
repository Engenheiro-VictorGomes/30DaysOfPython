# 5. Calculate the time difference between 1 January 1970 and now.
from datetime import datetime

now = datetime.now()
date = datetime.strptime("1 January 1970", "%d %B %Y")

diff = now-date
print(diff)
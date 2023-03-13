# 4. Calculate the time difference between now and new year.
from datetime import datetime

now = datetime.now()
newYear = datetime.strptime("31/12/2022 23:59:59", "%d/%m/%Y %H:%M:%S")

diff = now-newYear
print(diff)
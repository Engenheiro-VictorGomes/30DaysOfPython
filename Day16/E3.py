# 3. Today is 5 December, 2019. Change this time string to time.
from datetime import datetime
myString = "5 December, 2019"
print(datetime.strptime(myString, "%d %B, %Y"))

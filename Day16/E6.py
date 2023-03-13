# 6. Think, what can you use the datetime module for? Examples:
#     Time series analysis
#     To get a timestamp of any activities in an application
#     Adding posts on a blog

# datetime: signal value
from datetime import datetime

now = datetime.now()
signal = {now.strftime("%m/%d/%Y %H:%M:%S.")+str(n):n for n in range(1000)}
print(signal)

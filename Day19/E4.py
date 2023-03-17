# 4. Extract all incoming email addresses as a list from the email_exchange_big.txt file.

import re

email_regex = r'\s+[[a-zA-Z]+[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]+\.+[a-zA-Z0-9]+\s'
filepath = './data/email_exchanges_big.txt'
mails = set()
with open(filepath) as file:
    for line in file:
        mail = re.findall(email_regex,line.strip())
        for m in mail:
            mails.add(m)

for mail in mails:
    print(mail)

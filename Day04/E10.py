# 10.	Check if Coding For All string contains a word Coding using the method index, find or other methods.
company = ' for All'
try:
    print(company.index('Coding'))
except ValueError:
    print("Not found")

try:
    print(company.find('Coding'))
except ValueError:
    print("Not found")


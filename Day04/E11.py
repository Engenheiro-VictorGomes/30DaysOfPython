# 11.	Replace the word coding in the string 'Coding For All' to Python.
company = 'Coding for All'
try:
    print(company.replace('Coding', 'Python'))
except ValueError:
    print("Not found")

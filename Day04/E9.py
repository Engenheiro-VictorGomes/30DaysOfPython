# 9.	Cut(slice) out the first word of Coding For All string.
expected = ' for All'

# Solution:
company = 'Coding for All'
company = company.strip('Coding')
print(f"Result = {company == expected}")
# 19.	Create an acronym or an abbreviation for the name 'Coding For All'.
expected = 'CFA'
mystring = 'Coding For All'

# Solution 01
acronym = ''
for piece in mystring.split():
    acronym += piece[0]
print(f"Solution 01 result = {acronym == expected}")

# Solution 02
acronym = ''.join([piece[0] for piece in mystring.split()])
print(f"Solution 02 result = {acronym == expected}")
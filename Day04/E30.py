# 30.	'   Coding For All      '  , remove the left and right trailing spaces in the given string.

stringExpected = 'Coding For All'

# Solution 01
myString = '   Coding For All      '
myString = myString.strip(' ')
print(myString)
print(f"Result: {myString == stringExpected}")

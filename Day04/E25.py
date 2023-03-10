# 25.	Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
expected = 'You cannot end a sentence with is a conjunction'
mystring = 'You cannot end a sentence with because because because is a conjunction'
sliceString = 'because because because'

# Solution 01:
resultString = mystring.replace(sliceString, '')
resultString = resultString.replace('  ', ' ')
print(f"Result Solution 01 = {resultString == expected}")

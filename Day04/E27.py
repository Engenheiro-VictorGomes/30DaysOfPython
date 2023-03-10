# 27.	Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
mystring = 'You cannot end a sentence with because because because is a conjunction'
sliceString = 'because because because'
resultString = mystring.replace(sliceString, '')
print(resultString)
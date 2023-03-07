# There is no 'on' in both dragon and python

string1 = "python"
string2 = "dragon"

checkString1 = string1.__contains__('on')
checkString2 = string2.__contains__('on')

print(not checkString1)
print(not checkString2)
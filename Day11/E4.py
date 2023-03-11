# 4. Write a function which check if provided variable is a valid python variable

def checkStringName(stringName):
    return stringName.isidentifier()

stringName = 'validName'
assert checkStringName(stringName) == True, 'Fail'
stringName = '!NotaValidName#@'
assert checkStringName(stringName) == False, 'Fail'
print("checkStringName() works")
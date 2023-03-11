# 3. Write a function which checks if all the items of the list are of the same data type.

def allSameType(list):
    typeList = [type(item) for item in list]
    return len(set(typeList)) == 1

list = ['2','3','4','5','21','12','8']
assert allSameType(list) == True, 'Fail'
list = ['2','3','4','5','21','12','8',8]
assert allSameType(list) == False, 'Fail'
print("allSameType() works")
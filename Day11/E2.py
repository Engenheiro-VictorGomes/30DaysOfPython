# 2. Write a functions which checks if all items are unique in the list.

def allUnique(list):
    return len(set(list)) == len(list)

list = ['2','3','4','5','21','12','8']
assert allUnique(list) == True, 'Fail'
list = ['2','3','4','5','21','12','8','8']
assert allUnique(list) == False, 'Fail'
print("allUnique() works")
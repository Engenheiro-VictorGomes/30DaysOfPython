# 16. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(myList):
    result = []
    for item in myList:
        if isinstance(item, str):
            result.append(item)
    return result

myList = [1,2,'aa','bb']
expected = ['aa','bb']

output = get_string_lists(myList)
print(f"Test ok? {output == expected}")

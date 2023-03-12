# 1. Filter only negative and zero in the list using list comprehension
#     numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers = [i if i>0 else 0 for i in numbers]
print(numbers)
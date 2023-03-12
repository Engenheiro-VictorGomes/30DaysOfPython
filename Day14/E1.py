# 1. Explain the difference between map, filter, and reduce.

# map uses a function and iterable, and return an iterator with the result of the function for each element of the iterable
# Example:
countries = ['norway', 'brasil', 'italy']
Countries = list(map(lambda x: x[0].upper()+x[1:], countries))
# Countries = ['Norway', 'Brasil', 'Italy']
print(Countries)

# filter uses a bool function and iterable, to return iterator with the elements which the function is true
numbers = [i for i in range(100)]
odd_number = list(filter(lambda x: x % 2, numbers))
print(odd_number)

# reduce uses function with 2 args, and iterable, apply the funcion for each pair and return one value
from functools import reduce
numbers = [i for i in range(101)]
sum = reduce(lambda x,y:x+y, numbers)
print(sum)
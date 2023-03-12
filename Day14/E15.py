# 15. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

map_callback = lambda country: country.upper()
filter_callback = lambda country: country[0] == 'E'
reduce_callback = lambda acc, val: acc + len(val)
result = reduce(reduce_callback, filter(filter_callback, map(map_callback, countries)))

print(result)
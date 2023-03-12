# 23. Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
#     Sort countries by name, by capital, by population
#     Sort out the ten most spoken languages by location.
#     Sort out the ten most populated countries.

import json

with open('countries_data.json') as f:
    countries_data = json.load(f)

print(sorted(countries_data, key=lambda k: k['name']))
print(sorted(countries_data, key=lambda k: k['capital']))
print(sorted(countries_data, key=lambda k: k['population']))

result = [language for country in countries_data for language in country['languages']]
dict1 = {}
for language in result:
    if language in dict1:
        dict1[language] += 1
    else:
        dict1[language] = 1
sorted_list = list(sorted(dict1.items(), key=lambda item: item[1], reverse=True))[:10]
sorted_list = [name[0] for name in sorted_list]
print(sorted_list)

print(sorted(countries_data, key=lambda k: k['population'])[10:])

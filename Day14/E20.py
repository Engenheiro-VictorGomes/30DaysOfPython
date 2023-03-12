# 20. Create a function returning a dictionary, where keys stand for starting letters of countries
# and values are the number of country names starting with that letter.

import json

def categorize_countries(countries):
    result = {}
    for country in countries:
        letter = country['name'][0]
        if letter in result:
            result[letter] += 1
        else:
            result.update({letter:1})
    return result

with open('countries_data.json') as f:
    countries_data = json.load(f)
print(categorize_countries(countries_data))

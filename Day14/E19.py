# 19. Declare a function called categorize_countries that returns a list of countries with some common pattern
# (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).

import json

def categorize_countries(countries, pattern):
    result = []
    for country in countries:
        if country['name'].find(pattern) != -1:
            result.append(country['name'])
    return result

with open('countries_data.json') as f:
    countries_data = json.load(f)
print(categorize_countries(countries_data,'land'))
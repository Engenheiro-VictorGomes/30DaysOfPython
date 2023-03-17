# 3. Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
# 
#     # Your output should look like this
#     print(most_populated_countries(filename='./data/countries_data.json', 10))
# 
#     [
#     {'country': 'China', 'population': 1377422166},
#     {'country': 'India', 'population': 1295210000},
#     {'country': 'United States of America', 'population': 323947000},
#     {'country': 'Indonesia', 'population': 258705000},
#     {'country': 'Brazil', 'population': 206135893},
#     {'country': 'Pakistan', 'population': 194125062},
#     {'country': 'Nigeria', 'population': 186988000},
#     {'country': 'Bangladesh', 'population': 161006790},
#     {'country': 'Russian Federation', 'population': 146599183},
#     {'country': 'Japan', 'population': 126960000}
#     ]
# 
#     # Your output should look like this
# 
#     print(most_populated_countries(filename='./data/countries_data.json', 3))
#     [
#     {'country': 'China', 'population': 1377422166},
#     {'country': 'India', 'population': 1295210000},
#     {'country': 'United States of America', 'population': 323947000}
#     ]
# 

import json

def most_populated_countries(filename = None, n=10):
    if filename is None:
        raise ValueError
    if n <= 0:
        raise ValueError
    filepath = filename
    with open(filepath) as file:
        countries = json.load(file)
    countries = sorted(countries,key=lambda x: x['population'], reverse=True)[:n]
    return [{'name': country['name'], 'population': country['population']} for country in countries]

print(most_populated_countries(filename='./data/countries_data.json', n=10))
print(most_populated_countries(filename='./data/countries_data.json', n=3))
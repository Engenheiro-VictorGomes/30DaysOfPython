# 5. Go to the data folder and access the countries-data.py file.
#     Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
#     Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.

import json

with open('countries_data.json') as f:
    countries_data = json.load(f)

def most_spoken_languages(countries_data,n):
    languages = {}
    for country in countries_data:
        for language in country['languages']:
            if language in languages:
                languages[language] += 1
            else:
                languages[language] = 1
    mostSpoken = sorted(languages, key=lambda x: languages[x], reverse=True)
    return mostSpoken[:n]
print(most_spoken_languages(countries_data,5))


def most_populated_countries(countries_data, n):
    result = []
    sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    result = [country['name'] for country in sorted_countries[:n]]
    return result

print(most_populated_countries(countries_data,5))
# 21. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
import json

def get_first_ten_countries(countries,n):
    result = []
    for country in countries:
        result.append(country['name'])
    return result[:n]

with open('countries_data.json') as f:
    countries_data = json.load(f)
print(get_first_ten_countries(countries_data,10))


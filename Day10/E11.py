# 11. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
import Countries

countries = Countries.countries

# Solution 01
for country in countries:
    if country.__contains__('land'):
        print(country)

# Solution 02:
result = list(filter(lambda country: 'land' in country, countries))
print(result)
# 13. Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
# Find the ten most spoken languages from the data
# Find the 10 most populated countries in the world

# No py file, only json.
import json

with open('countries_data.json') as f:
    countries_data = json.load(f)

languages = set()
notUniqueTotal = 0
for country in countries_data:
    if 'languages' in country:
        for lang in country['languages']:
            languages.add(lang)
            notUniqueTotal += 1
print(f"What are the total number of languages in the data? (total) {notUniqueTotal}")
print(f"What are the total number of languages in the data? (unique) {len(languages)}")

languages = {}
for country in countries_data:
    for language in country['languages']:
        if language in languages:
            languages[language] += 1
        else:
            languages[language] = 1
mostSpoken = max(languages, key=languages.get)
print(f"Find the ten most spoken languages from the data = {mostSpoken}")


print("Find the 10 most populated countries in the world")
sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
for i, country in enumerate(sorted_countries[:10]):
    print(f"{i+1}.{country['name']}")
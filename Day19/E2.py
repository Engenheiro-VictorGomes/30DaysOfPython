# 2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
#     # Your output should look like this
#     print(most_spoken_languages(filename='./data/countries_data.json', 10))
#     [(91, 'English'),
#     (45, 'French'),
#     (25, 'Arabic'),
#     (24, 'Spanish'),
#     (9, 'Russian'),
#     (9, 'Portuguese'),
#     (8, 'Dutch'),
#     (7, 'German'),
#     (5, 'Chinese'),
#     (4, 'Swahili'),
#     (4, 'Serbian')]
# 
#     # Your output should look like this
#     print(most_spoken_languages(filename='./data/countries_data.json', 3))
#     [(91, 'English'),
#     (45, 'French'),
#     (25, 'Arabic')]
# 
import json

def most_spoken_languages(filename = None, n=10):
    if filename is None:
        raise ValueError
    if n <= 0:
        raise ValueError
    filepath = filename
    with open(filepath) as file:
        countries = json.load(file)
    language_count = {}
    for country in countries:
        for language in country['languages']:
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1
    return(sorted([(count, language) for language, count in language_count.items()], reverse=True)[:n])

print(most_spoken_languages(filename='./data/countries_data.json', n=10))
print(most_spoken_languages(filename='./data/countries_data.json', n=3))


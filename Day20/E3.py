# 3. Read the countries API and find
#     the 10 largest countries
#     the 10 most spoken languages
#     the total number of languages in the countries API

import requests

# Open the API
url = 'https://restcountries.eu/rest/v2/all'
response = requests.get(url)  # opening a network and fetching a data
print(response.status_code)  # status code, success:200
if response.status_code:
    countries = response.json()
    print(countries[1:])

# Not possible to finish, due a "Connection refused" error.
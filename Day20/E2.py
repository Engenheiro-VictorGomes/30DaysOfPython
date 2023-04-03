# 2. Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
#     the min, max, mean, median, standard deviation of cats' weight in metric units.
#     the min, max, mean, median, standard deviation of cats' lifespan in years.
#     Create a frequency table of country and breed of cats

import requests
import re

# Open the API
url = 'https://api.thecatapi.com/v1/breeds'  # countries api
response = requests.get(url)  # opening a network and fetching a data
cats = response.json()

# Get the information from the json
weights = []
lifespans = []
countries = []
breeds = []
for cat in cats:
    weights.append(cat['weight']['metric'])
    lifespans.append(cat['life_span'])
    countries.append(cat['origin'])
    breeds.append(cat['name'])

# extract the weight min and max
pattern = r"(\d+)\s+-\s+(\d+)"
weight_metrics = []
weight_results = {}
for weight in weights:
    line = re.search(pattern, weight)
    if line:
        weight_metrics.append(int(line.group(1)))
        weight_metrics.append(int(line.group(2)))
weight_metrics.sort()
weight_results['min'] = min(weight_metrics)
weight_results['max'] = max(weight_metrics)
weight_results['mean'] = sum(weight_metrics)/len(weight_metrics)
weight_results['median'] = weight_metrics[int(len(weight_metrics)/2)]
weight_results['standard_deviation'] = sum(list(map(lambda x: ((x-weight_results['median'])**2), weight_metrics)))**(1/2)/len(weight_metrics)

# extract the life min and max
life_years = []
lifespan_results = {}
for lifespan in lifespans:
    line = re.search(pattern, lifespan)
    if line:
        life_years.append(int(line.group(1)))
        life_years.append(int(line.group(2)))
life_years.sort()      
lifespan_results['min'] = min(life_years)
lifespan_results['max'] = max(life_years)
lifespan_results['mean'] = sum(life_years)/len(life_years)
lifespan_results['median'] = life_years[int(len(life_years)/2)]
lifespan_results['standard_deviation'] = sum(list(map(lambda x: ((x-lifespan_results['median'])**2), life_years)))**(1/2)/len(life_years)

countries_count = {}
for country in countries:
    if country in countries_count:
        countries_count[country]+=1
    else:
        countries_count[country]=1

breeds_count = {}
for breed in breeds:
    if breed in breeds_count:
        breeds_count[breed]+=1
    else:
        breeds_count[breed]=1

print(weight_results)
print(lifespan_results)
print(countries_count)
print(breeds_count)
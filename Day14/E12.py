# 12. Use filter to filter out countries having exactly six characters.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
countries_land = list(filter(lambda x: len(x)==6, countries))
print(countries_land)
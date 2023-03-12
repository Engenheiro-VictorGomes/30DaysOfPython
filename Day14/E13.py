# 13. Use filter to filter out countries containing six letters and more in the country list.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
countries_land = list(filter(lambda x: len(x)>=6, countries))
print(countries_land)
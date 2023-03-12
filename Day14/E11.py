# 11. Use filter to filter out countries containing 'land'.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
countries_land = list(filter(lambda x: x.__contains__('land'), countries))
print(countries_land)
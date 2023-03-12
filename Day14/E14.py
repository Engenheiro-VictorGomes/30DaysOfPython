# 14. Use filter to filter out countries starting with an 'E'
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
countries_land = list(filter(lambda x: x[0]=='E', countries))
print(countries_land)
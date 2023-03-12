# 8. Use map to create a new list by changing each country to uppercase in the countries list
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
newcountries = list(map(lambda x: x.upper(), countries))
print(newcountries)
# 5.Change the following list to a list of dictionaries:
#     countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#     output:
#     [{'country': 'FINLAND', 'city': 'HELSINKI'},
#     {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#     {'country': 'NORWAY', 'city': 'OSLO'}]

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
expected = [
     {'country': 'FINLAND', 'city': 'HELSINKI'},
     {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
     {'country': 'NORWAY', 'city': 'OSLO'}]

output = [{'country': country[0].upper(), 'city': country[1].upper()} for list in countries for country in list]
print(f"Code worked? {output == expected}")
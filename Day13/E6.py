# 6.Change the following list of lists to a list of concatenated strings:
#     names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
#     output
#     ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

names = [[('Asabeneh', 'Yetaeyeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
expected = ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
output = [name[0]+' '+name[1] for list in names for name in list]
print(f"Code worked? {output == expected}")
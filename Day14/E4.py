# 4. Define a call function before map, filter or reduce, see examples.
def upperFirstLetter(word):
    return word[0].upper()+word[1:]

countries = ['norway', 'brasil', 'italy']
Countries = list(map(upperFirstLetter, countries))
# Countries = ['Norway', 'Brasil', 'Italy']
print(Countries)
# 18. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
myString = reduce(lambda x,y: x+', '+y,countries)
myString += " are north European countries"
myString = myString.replace(', Iceland',' and Iceland',1)
print(myString)

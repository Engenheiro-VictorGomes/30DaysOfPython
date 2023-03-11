# 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
myString = "I am a teacher and I love to inspire and teach people."
mySet = set(myString.split(' '))
print(myString.split(' '))
print(f"myString size = {len(myString.split())}, unique words = {len(mySet)}")
print(mySet)
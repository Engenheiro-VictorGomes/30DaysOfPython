# 7. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
import random

def sevenRandom():
    mySet = set()
    while len(mySet) < 7:
        mySet.add(random.randint(0,9))
    return list(mySet)

print(sevenRandom())
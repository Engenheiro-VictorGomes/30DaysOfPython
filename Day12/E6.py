# 6. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
import random

def shuffle_list(input_list):
    shuffled = input_list.copy()
    filled = set(range(len(input_list)))
    for item in input_list:
        random_index = random.choice(list(filled))
        shuffled[random_index] = item
        filled.remove(random_index)
    return shuffled

myList = [1,2,3,4,5,6,7,8,9]
print(f"Original list = {myList}")
print(f"Shuffled list = {shuffle_list(myList)}")

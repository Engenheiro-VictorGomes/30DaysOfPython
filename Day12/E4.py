# 4. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

import random

def list_of_rgb_colors(rept):
    result = []
    for i in range(rept):
        myColor = []
        for j in range(3):
            myColor.append(random.randint(0,255))
        result.append(f"{myColor}")
    return result

print(list_of_rgb_colors(5))
# 3. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array
#   (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols,
#    0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

import random
import string

def list_of_hexa_colors(rept):
    result = []
    for i in range(rept):
        myColor = ''
        for j in range(6):
            myColor += string.hexdigits[random.randint(0,15)]
        result.append(f"#{myColor}")
    return result

print(list_of_hexa_colors(5))
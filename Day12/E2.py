# 2. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
# print(rgb_color_gen())
# # rgb(125,244,255) - the output should be in this form
# 
import random

def rgb_color_gen():
    return f"rgb({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)})"
print(rgb_color_gen())
# 5. Write a function generate_colors which can generate any number of hexa or rgb colors.
#    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
#    generate_colors('hexa', 1) # ['#b334ef']
#    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
#    generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
# 
import random
import string

def generate_hexa_colors():
    myColor = ''
    for j in range(6):
        myColor += string.hexdigits[random.randint(0,15)]
    return f"#{myColor}"

def generate_rgb_colors():
    myColor = '('
    for j in range(3):
        myColor += str(random.randint(0,255)) + ','
    myColor = myColor[:-1]
    return f"rgb{myColor})"

def generate_colors(formatColor, rept):
    result = []
    for i in range(rept):
        if formatColor == 'hexa':
            result.append(generate_hexa_colors())
        elif formatColor == 'rgb':
            result.append(generate_rgb_colors())
        else:
            raise ValueError
    print(result)
    return result


generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
generate_colors('hexa', 1) # ['#b334ef']
generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
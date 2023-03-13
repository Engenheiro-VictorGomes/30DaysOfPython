# 1. Open you python interactive shell and try all the examples covered in this section.

#SyntaxError
#print 'hello world'    #Not possible to use try/except
pass


#NameError
try:
    print(age)
except NameError:
    print("Name Error")

#IndexError
numbers = [1, 2, 3, 4, 5]
try:
    numbers[5]
except IndexError:
    print("Index Error")

#ModuleNotFoundError
try:
    import maths
except ModuleNotFoundError:
    print("Module Not Found Error")

#AttributeError
import math
try:
    math.PI
except AttributeError:
    print("Attribute Error")

#KeyError
users = {'name':'Asab', 'age':250, 'country':'Finland'}
try:
    users['name']
except KeyError:
    print("Key Error")

#TypeError
try:
    4 + '3'
except TypeError:
    print("Type Error")

#ImportError
try:
    from math import power
except ImportError:
    print("Import Error")

#ValueError
try:
    int('12a')
except ValueError:
    print("Value Error")

#ZeroDivisionError
try:
    1/0
except ZeroDivisionError:
    print("Zero Division Error")
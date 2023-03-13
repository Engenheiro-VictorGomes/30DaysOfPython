# 3. Write a pattern which identifies if a string is a valid python variable
#     is_valid_variable('first_name') # True
#     is_valid_variable('first-name') # False
#     is_valid_variable('1first_name') # False
#     is_valid_variable('firstname') # True
import re

def is_valid_variable(variable_name):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return re.match(pattern, variable_name) is not None

assert is_valid_variable('first_name') == True
assert is_valid_variable('first-name') == False
assert is_valid_variable('1first_name') == False
assert is_valid_variable('firstname') == True
print("is_valid_variable() works")
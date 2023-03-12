# 1. Write a function which generates a six digit/character random_user_id.
#   print(random_user_id());
#   '1ee33d'
# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input().
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
# print(user_id_gen_by_user()) # user input: 5 5
# #output:
# #kcsy2
# #SMFYb
# #bWmeq
# #ZXOYh
# #2Rgxf
#    
# print(user_id_gen_by_user()) # 16 5
# #1GCSgPLMaBAVQZ26
# #YD7eFwNQKNs7qXaT
# #ycArC5yrRupyG00S
# #UbGxOFI7UXSWAyKN
# #dIV0SSUTgAdKwStr

import random
import string

def random_user_id(size):
    result = ''
    for i in range(size):
        result += (string.ascii_letters + string.digits)[random.randint(0, len(string.ascii_letters + string.digits)-1)]
    return result

print(random_user_id(6))


def user_id_gen_by_user():
    size = input("Enter the size of the ID: ")
    rept = input("Enter how many IDs you need: ")
    for i in range(int(rept)):
        print(random_user_id(int(size)))

user_id_gen_by_user()
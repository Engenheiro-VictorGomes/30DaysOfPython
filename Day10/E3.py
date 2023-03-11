# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
# 
#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######

myString = ''
for i in range(7):
    myString += '#'
    print(myString)
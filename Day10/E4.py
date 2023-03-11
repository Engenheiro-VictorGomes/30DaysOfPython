# 4. Use nested loops to create the following:
# 
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #

myLine = ''
for line in range(8):
    for column in range(8):
        myLine += '#'
    print(myLine)
    myLine = ''
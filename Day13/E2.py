# 2. Flatten the following list of lists of lists to a one dimensional list :
#     list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
#     output= [1, 2, 3, 4, 5, 6, 7, 8, 9]
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
output = [i for j in list_of_lists for z in j for i in z]
print(output)
print(f"Code worked? {output == expected}")
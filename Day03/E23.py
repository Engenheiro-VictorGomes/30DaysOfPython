# Write a Python script that displays the following table
#    1 1 1 1 1
#    2 1 2 4 8
#    3 1 3 9 27
#    4 1 4 16 64
#    5 1 5 25 125

reference = [
    [1,1,1,1,1],
    [2,1,2,4,8],
    [3,1,3,9,27],
    [4,1,4,16,64],
    [5,1,5,25,125]]

# Solution 01:
table = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]]
row = 0
col = 0
for rows in table:
    for cell in rows:
        if row == 0:
            table[row][col] = 1
        elif col == 0:
            table[row][col] = (row+1)**(col+1)
        elif col == 1:
            table[row][col] = 1
        else:
            table[row][col] = (row+1)**(col-1)
        col += 1
    col = 0
    row += 1
testingResult = (table == reference)
print(f"Testing result (Solution 01) = {testingResult}")

# Solution 02:
table = [[0]*5 for _ in range(5)]
for row in range(len(table)):
    for col in range(len(table[row])):
        if col == 0:
            table[row][col] = (row+1)**(col+1)
        else:
            table[row][col] = (row+1)**(col-1)
testingResult = (table == reference)
print(f"Testing result (Solution 02) = {testingResult}")

# Solution 03:
table = [[0]*5 for _ in range(5)]
for row in range(len(table)):
    table[row][:] = [(row+1)**abs(col-1) for col in range(len(table[row]))]
testingResult = (table == reference)
print(f"Testing result (Solution 03) = {testingResult}")

# Solution 04:
table = [[(row+1)**abs(col-1) for col in range(5)] for row in range(5)]
testingResult = (table == reference)
print(f"Testing result (Solution 04) = {testingResult}")
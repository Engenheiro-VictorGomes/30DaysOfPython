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
    [5,1,5,25,125]
]

table = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]


row = 0
col = 0

for rows in table:
    for cell in rows:
        if row == 0:
            table[row][col] = 1
        elif col == 1:
            table[row][col] = 1
        else:
            cell = (row+1)**(col+1)
        col += 1
    row += 1
    print(rows)

testingResult = (table == reference)
print(f"Testing result = {testingResult}")
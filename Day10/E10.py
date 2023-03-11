# 10. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.

oddSum = 0
evenSum = 0
for i in range(101):
    if i%2:
        evenSum += i
    else:
        oddSum += i

print(f"Odd sum = {oddSum}, even sum = {evenSum}.")
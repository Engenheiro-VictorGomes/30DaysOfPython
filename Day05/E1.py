# 1.	The following is a list of 10 students ages:
# 	ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 	Sort the list and find the min and max age
ages.sort()
print(f"Sorted = {ages}")
print(f"Max = {max(ages)}")
print(f"Min = {min(ages)}")

# 	Add the min age and the max age again to the list
ages.append(max(ages))
ages.append(min(ages))
ages.sort()
print(f"New Sorted = {ages}")

# 	Find the median age (one middle item or two middle items divided by two)
if len(ages)%2:
    index1 = len(ages)/2
    index1 = int(index1)
    print(f"Median = {ages[index1]}")
else:
    index1 = len(ages)/2
    index1 = int(index1)
    index2 = (len(ages)-1)/2
    index2 = int(index2)
    print(f"Median = {ages[index1]} and {ages[index2]}")

# 	Find the average age (sum of all items divided by their number )
average = sum(ages)/len(ages)
print(f"Average = {average}")

# 	Find the range of the ages (max minus min)
range = max(ages) - min(ages)
print(f"Range = {range}")

# 	Compare the value of (min - average) and (max - average), use abs() method
dmin = abs(min(ages) - average)
dmax = abs(max(ages) - average)
print(f"(min - average) = {dmin} | (max - average) = {dmax}")

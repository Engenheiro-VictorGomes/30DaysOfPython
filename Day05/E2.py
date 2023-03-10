# 2. Find the middle country(ies) in the countries list
# 	Divide the countries list into two equal lists if it is even if not one more country for the first half.
# 	['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
# 

# List into two equal lists if it is even if not one more country for the first half.
expected1 = ['China', 'Russia', 'USA', 'Finland'],['Sweden', 'Norway', 'Denmark']
Countries1 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
expected2 = ['China', 'Russia', 'USA'],['Sweden', 'Norway', 'Denmark']
Countries2 = ['China', 'Russia', 'USA', 'Sweden', 'Norway', 'Denmark']

print("Exercise 01:")
# Solution 01
list1 = []
list2 = []
for i, Country in enumerate(Countries1):
    if i < len(Countries1)/2:
        list1.append(Country)
    else:
        list2.append(Country)
result = list1,list2
print(f"             Solution 01, case01 test result = {result == expected1}")

list1 = []
list2 = []
for i, Country in enumerate(Countries2):
    if i < len(Countries2)/2:
        list1.append(Country)
    else:
        list2.append(Country)
result = list1,list2
print(f"             Solution 01, case02 test result = {result == expected2}")

# Solution 02
result = Countries1[:int((len(Countries1)+1)/2)],Countries1[int((len(Countries1)+1)/2):]
print(f"             Solution 02, case01 test result = {result == expected1}")
result = Countries2[:int((len(Countries2)+1)/2)],Countries2[int((len(Countries2)+1)/2):]
print(f"             Solution 02, case02 test result = {result == expected2}")

#Solution 03
middlePos = int((len(Countries1)+1)/2)
result = Countries1[:middlePos],Countries1[middlePos:]
print(f"             Solution 03, case01 test result = {result == expected1}")
middlePos = int((len(Countries2)+1)/2)
result = Countries2[:middlePos],Countries2[middlePos:]
print(f"             Solution 03, case02 test result = {result == expected2}")

# Unpack the first three countries and the rest as scandic countries.
print("Exercise 02:")

# Solution 01
expected1 = ['China', 'Russia', 'USA'],[ 'Finland', 'Sweden', 'Norway', 'Denmark']
expected2 = ['China', 'Russia', 'USA'],[ 'Sweden', 'Norway', 'Denmark']
unpack = Countries1[:3]
scandic = Countries1[3:]
print(f"             Solution 01, case 01, test result = {expected1 == (unpack,scandic)}")
unpack = Countries2[:3]
scandic = Countries2[3:]
print(f"             Solution 01, case 02, test result = {expected2 == (unpack,scandic)}")
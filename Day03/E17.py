# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = 10
if not number % 2:
    print(f"{number} is Even")
else:
    print(f"{number} is not even")

number = 11
if not number % 2:
    print(f"{number} is Even")
else:
    print(f"{number} is not even")

# Solution 02:
number = 10
print(f"{number} is even? {number % 2}")

number = 11
print(f"{number} is even? {number % 2}")

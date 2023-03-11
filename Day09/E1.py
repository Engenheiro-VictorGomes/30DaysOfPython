# 1.0 Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
#     Enter your age: 30
#     You are old enough to learn to drive.
#     Output:
#     Enter your age: 15
#     You need 3 more years to learn to drive.
age = None
while age is None:
    try:
        age = int(input("Enter your age: "))
        if age<0:
            raise ValueError
    except ValueError:
        print("Not a valid age, try again.")
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    wait = 18-age
    print(f"You need {wait} more year{'s' if wait-1 else ''} to learn to drive.")

# 1.1 Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
#     Enter your age: 30
#     You are 5 years older than me.
#     Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
#     Enter number one: 4
#     Enter number two: 3
#     4 is greater than 3
myAge = 32
yourAge = None
while yourAge is None:
    try:
        yourAge = int(input("Enter your age: "))
        if yourAge<0:
            raise ValueError
    except ValueError:
        print("Not a valid age, try again.")
if myAge == yourAge:
    print(f"We have the same age.")
elif myAge > yourAge:
    diff = myAge - yourAge
    print(f"I'm {diff} year{'s' if diff-1 else ''} older than you.")
else:
    diff = yourAge - myAge
    print(f"You are {diff} year{'s' if diff-1 else ''} older than me.")

vInteger = 1
vFloat = 1.0
vComplex = 1.1 + 1.2j
vString = "String"
vBoolean = True
vList = [1,2,3,4,5]
vTuple = ('Earth', 'Jupiter', 'Neptune', 'Mars', 'Venus', 'Saturn', 'Uranus', 'Mercury')
vSet = {3.14, 9.81, 2.7}
vDictionary = {
    'Name':'square_1',
    'Color':'blue',
    'xSize':5,
    'ySize':5,
}

# Check the data type of all your variables using type() built-in function
print(type(vInteger))
print(type(vFloat))
print(type(vComplex))
print(type(vString))
print(type(vBoolean))
print(type(vList))
print(type(vTuple))
print(type(vSet))
print(type(vDictionary))

# Using the len() built-in function, find the length of your first name
print(len("Victor"))

# Compare the length of your first name and your last name
print(len("Gomes"))
print(max(len("Victor"), len("Gomes")))
print(min(len("Victor"), len("Gomes")))

# Declare 5 as num_one and 4 as num_two
#   Add num_one and num_two and assign the value to a variable total
#   Subtract num_two from num_one and assign the value to a variable diff
#   Multiply num_two and num_one and assign the value to a variable product
#   Divide num_one by num_two and assign the value to a variable division
#   Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
#   Calculate num_one to the power of num_two and assign the value to a variable exp
#   Find floor division of num_one by num_two and assign the value to a variable floor_division
num_one = 5
num_two = 4
total = num_one + num_two
print(f"Total = {total}")
diff = num_two - num_one
print(f"Diff = {diff}")
product = num_two * num_one
print(f"Product = {product}")
division = num_one / num_two
print(f"Division = {division}")
remainder = num_one % num_two
print(f"Remainder = {remainder}")
exp = num_one ** num_two
print(f"Exp = {exp}")
floor_division = int(num_one/num_two)
print(f"Floor Division = {floor_division}")

# The radius of a circle is 30 meters.
#   Calculate the area of a circle and assign the value to a variable name of area_of_circle
#   Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
#   Take radius as user input and calculate the area.
radius = 30
area_of_circle = 3.14*radius**2
print(f"area of a circle = {area_of_circle}")
circum_of_circle = 2*radius*3.14
print(f"circumference of a circle = {circum_of_circle}")
userInput = float(input("Enter the radius"))
area_of_circle = 3.14*userInput**2
print(f"area of a circle = {area_of_circle}")

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
#TODO

# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
#TODO

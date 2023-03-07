# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

# Using for and if
for i in range(-100, 100):
    x = i/10
    y = x**2 + 6*x + 9
    if y == 0:
        print(f"Possible result x = {x}")

# Just math
# y = ax^2 + bx + c
a = 1
b = 6
c = 9

delta = b**2 - 4*a*c
if delta < 0:
    print("No real answer.")
elif delta == 0:
    x = (-b + (delta)**(1/2))/2*a
    print (f"Possible result: x = {x}")
else:
    x = (-b + (delta)**(1/2))/2*a
    print (f"Possible result: x = {x}")
    x = (-b - (delta)**(1/2))/2*a
    print (f"Possible result: x = {x}")        
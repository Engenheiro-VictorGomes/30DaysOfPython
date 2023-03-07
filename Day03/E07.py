# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

radius = float(input("Enter the radius: "))
area = 3.14 * radius**2
circumference = 2 * 3.14 * radius
print(f"The area is {area}")
print(f"The circumference is {circumference}")
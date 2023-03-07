# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
perimeter = 2*(length + width)
print(f"The area of the rectangle is {area}")
print(f"The perimeter of the rectangle is {perimeter}")
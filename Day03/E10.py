# Compare the slopes in tasks 8 and 9.

# Q8
a = 2
b = -2
xIntercept = -b/a
yIntercept = b
print(f"Q8. X Intercept = {xIntercept}")
print(f"Q8. Y Intercept = {yIntercept}")

# Q9
point1 = (2,2)
point2 = (6,10)
slope = (point2[1] - point1[1])/(point2[0] - point1[0])
euclideanDistance = ((point2[1] - point1[1])**2 + (point2[0] - point1[0])**2)**(1/2)
print(f"Q9. Slope = {slope}")
print(f"Q9. Euclidean distance = {euclideanDistance}")

# Comparing
slopeQ8 = (yIntercept)/(xIntercept)
print(f"Slope Q8 = {slopeQ8}")
print(f"Slope Q9 = {slope}")

print(f"It's equal? {slopeQ8 == slope}")